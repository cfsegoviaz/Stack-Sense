#!/bin/bash

# API Portal - Deployment Script
# Automatiza el despliegue de infraestructura AWS usando CDK

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funciones de utilidad
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar prerrequisitos
check_prerequisites() {
    log_info "Verificando prerrequisitos..."
    
    # Verificar AWS CLI
    if ! command -v aws &> /dev/null; then
        log_error "AWS CLI no está instalado"
        exit 1
    fi
    
    # Verificar Node.js
    if ! command -v node &> /dev/null; then
        log_error "Node.js no está instalado"
        exit 1
    fi
    
    # Verificar CDK
    if ! command -v cdk &> /dev/null; then
        log_error "AWS CDK no está instalado. Ejecuta: npm install -g aws-cdk"
        exit 1
    fi
    
    # Verificar credenciales AWS
    if ! aws sts get-caller-identity &> /dev/null; then
        log_error "Credenciales AWS no configuradas"
        exit 1
    fi
    
    log_success "Prerrequisitos verificados"
}

# Instalar dependencias
install_dependencies() {
    log_info "Instalando dependencias..."
    npm install
    log_success "Dependencias instaladas"
}

# Bootstrap CDK (solo si es necesario)
bootstrap_cdk() {
    local account=$(aws sts get-caller-identity --query Account --output text)
    local region=${AWS_DEFAULT_REGION:-us-east-1}
    
    log_info "Verificando bootstrap CDK para cuenta $account en región $region..."
    
    # Verificar si ya está bootstrapped
    if aws cloudformation describe-stacks --stack-name CDKToolkit --region $region &> /dev/null; then
        log_info "CDK ya está bootstrapped"
    else
        log_info "Ejecutando bootstrap CDK..."
        cdk bootstrap aws://$account/$region
        log_success "Bootstrap CDK completado"
    fi
}

# Validar sintaxis
validate_syntax() {
    log_info "Validando sintaxis TypeScript..."
    npm run build
    log_success "Sintaxis validada"
}

# Generar templates CloudFormation
synthesize() {
    log_info "Generando templates CloudFormation..."
    cdk synth
    log_success "Templates generados en cdk.out/"
}

# Mostrar diferencias
show_diff() {
    local environment=$1
    log_info "Mostrando diferencias para ambiente $environment..."
    
    case $environment in
        "dev")
            cdk diff ApiPortalDevStack || true
            ;;
        "prod")
            cdk diff ApiPortalProdStack || true
            ;;
        *)
            log_error "Ambiente no válido: $environment"
            exit 1
            ;;
    esac
}

# Desplegar stack
deploy() {
    local environment=$1
    local auto_approve=${2:-false}
    
    log_info "Desplegando ambiente $environment..."
    
    # Mostrar diferencias primero
    show_diff $environment
    
    # Confirmar despliegue si no es automático
    if [ "$auto_approve" != "true" ]; then
        echo
        read -p "¿Continuar con el despliegue? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_warning "Despliegue cancelado"
            exit 0
        fi
    fi
    
    # Ejecutar despliegue
    case $environment in
        "dev")
            cdk deploy ApiPortalDevStack --require-approval never
            ;;
        "prod")
            cdk deploy ApiPortalProdStack --require-approval never
            ;;
        *)
            log_error "Ambiente no válido: $environment"
            exit 1
            ;;
    esac
    
    log_success "Despliegue completado para ambiente $environment"
}

# Destruir stack
destroy() {
    local environment=$1
    
    log_warning "¡ATENCIÓN! Vas a destruir el ambiente $environment"
    echo "Esto eliminará TODOS los recursos incluyendo:"
    echo "- Base de datos (se perderán los datos)"
    echo "- Buckets S3"
    echo "- Load Balancers"
    echo "- Servicios ECS"
    echo
    read -p "¿Estás SEGURO que quieres continuar? Escribe 'DELETE' para confirmar: " confirmation
    
    if [ "$confirmation" != "DELETE" ]; then
        log_warning "Destrucción cancelada"
        exit 0
    fi
    
    case $environment in
        "dev")
            cdk destroy ApiPortalDevStack --force
            ;;
        "prod")
            cdk destroy ApiPortalProdStack --force
            ;;
        *)
            log_error "Ambiente no válido: $environment"
            exit 1
            ;;
    esac
    
    log_success "Ambiente $environment destruido"
}

# Mostrar outputs del stack
show_outputs() {
    local environment=$1
    local stack_name
    
    case $environment in
        "dev")
            stack_name="ApiPortalDevStack"
            ;;
        "prod")
            stack_name="ApiPortalProdStack"
            ;;
        *)
            log_error "Ambiente no válido: $environment"
            exit 1
            ;;
    esac
    
    log_info "Outputs del stack $stack_name:"
    aws cloudformation describe-stacks \
        --stack-name $stack_name \
        --query 'Stacks[0].Outputs[*].[OutputKey,OutputValue,Description]' \
        --output table
}

# Mostrar ayuda
show_help() {
    echo "API Portal - Deployment Script"
    echo
    echo "Uso: $0 [COMANDO] [OPCIONES]"
    echo
    echo "Comandos:"
    echo "  check         Verificar prerrequisitos"
    echo "  install       Instalar dependencias"
    echo "  bootstrap     Bootstrap CDK"
    echo "  validate      Validar sintaxis"
    echo "  synth         Generar templates CloudFormation"
    echo "  diff ENV      Mostrar diferencias (dev|prod)"
    echo "  deploy ENV    Desplegar ambiente (dev|prod)"
    echo "  destroy ENV   Destruir ambiente (dev|prod)"
    echo "  outputs ENV   Mostrar outputs del stack (dev|prod)"
    echo "  full ENV      Ejecutar flujo completo (dev|prod)"
    echo
    echo "Opciones:"
    echo "  --auto-approve    No pedir confirmación para despliegue"
    echo "  --help           Mostrar esta ayuda"
    echo
    echo "Ejemplos:"
    echo "  $0 full dev                    # Despliegue completo desarrollo"
    echo "  $0 deploy prod --auto-approve  # Despliegue producción sin confirmación"
    echo "  $0 diff dev                    # Ver diferencias desarrollo"
    echo "  $0 outputs prod                # Ver outputs producción"
}

# Flujo completo
full_deployment() {
    local environment=$1
    local auto_approve=${2:-false}
    
    log_info "Iniciando despliegue completo para ambiente $environment"
    
    check_prerequisites
    install_dependencies
    bootstrap_cdk
    validate_syntax
    synthesize
    deploy $environment $auto_approve
    show_outputs $environment
    
    log_success "¡Despliegue completo exitoso!"
    echo
    echo "Próximos pasos:"
    echo "1. Verificar que todos los servicios estén funcionando"
    echo "2. Ejecutar pruebas de conectividad"
    echo "3. Configurar monitoreo y alertas"
    echo "4. Documentar endpoints y configuraciones"
}

# Procesar argumentos
case "${1:-help}" in
    "check")
        check_prerequisites
        ;;
    "install")
        install_dependencies
        ;;
    "bootstrap")
        bootstrap_cdk
        ;;
    "validate")
        validate_syntax
        ;;
    "synth")
        synthesize
        ;;
    "diff")
        if [ -z "$2" ]; then
            log_error "Especifica el ambiente: dev o prod"
            exit 1
        fi
        show_diff $2
        ;;
    "deploy")
        if [ -z "$2" ]; then
            log_error "Especifica el ambiente: dev o prod"
            exit 1
        fi
        auto_approve="false"
        if [ "$3" == "--auto-approve" ]; then
            auto_approve="true"
        fi
        deploy $2 $auto_approve
        ;;
    "destroy")
        if [ -z "$2" ]; then
            log_error "Especifica el ambiente: dev o prod"
            exit 1
        fi
        destroy $2
        ;;
    "outputs")
        if [ -z "$2" ]; then
            log_error "Especifica el ambiente: dev o prod"
            exit 1
        fi
        show_outputs $2
        ;;
    "full")
        if [ -z "$2" ]; then
            log_error "Especifica el ambiente: dev o prod"
            exit 1
        fi
        auto_approve="false"
        if [ "$3" == "--auto-approve" ]; then
            auto_approve="true"
        fi
        full_deployment $2 $auto_approve
        ;;
    "help"|"--help"|"-h")
        show_help
        ;;
    *)
        log_error "Comando no reconocido: $1"
        show_help
        exit 1
        ;;
esac