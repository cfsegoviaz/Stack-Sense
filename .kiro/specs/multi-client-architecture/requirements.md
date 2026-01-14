# Requirements Document

## Introduction

Stack Sense es una herramienta de diagnóstico y análisis para migraciones AWS (MAP - Migration Acceleration Program). Actualmente el proyecto tiene una estructura monolítica donde los datos del cliente BGR están mezclados con el código de análisis. Esta especificación define los requisitos para reorganizar el proyecto en una arquitectura multi-cliente con separación clara entre:

1. **Core Engine**: Motor de análisis y diagnóstico reutilizable
2. **Client Workspaces**: Espacios de trabajo aislados por cliente
3. **Presentation Layer**: Capa de presentación para mostrar resultados

## Glossary

- **Stack_Sense_Core**: Motor principal de análisis que procesa datos de assessment y genera recomendaciones
- **Client_Workspace**: Directorio aislado que contiene todos los datos, configuración y resultados de un cliente específico
- **Assessment_Data**: Datos de entrada provenientes de herramientas como RVTools, Cloudamize, Matilda
- **Migration_Wave**: Agrupación lógica de aplicaciones/servidores que se migrarán juntos en una fase
- **Business_Case**: Documento que justifica la migración con análisis de costos, ROI y beneficios
- **Presentation_App**: Aplicación web que muestra los resultados del análisis de forma visual e interactiva
- **Parser**: Componente que transforma datos de una fuente específica (RVTools, Cloudamize) a formato normalizado
- **Analyzer**: Componente que procesa datos normalizados y genera recomendaciones AWS

## Requirements

### Requirement 1: Multi-Client Workspace Management

**User Story:** As a migration consultant, I want to manage multiple client projects independently, so that I can work on different MAP assessments without data mixing.

#### Acceptance Criteria

1. WHEN a user creates a new client workspace THEN the Stack_Sense_Core SHALL generate a standardized directory structure with subdirectories for assessment data, analysis results, diagrams, and reports
2. WHEN a user lists available client workspaces THEN the Stack_Sense_Core SHALL display all configured clients with their status and last activity date
3. WHEN a user switches between client workspaces THEN the Stack_Sense_Core SHALL load the client-specific configuration and context
4. THE Stack_Sense_Core SHALL isolate each Client_Workspace data to prevent cross-contamination between clients
5. WHEN a client workspace is initialized THEN the Stack_Sense_Core SHALL create a configuration file with client metadata (name, industry, contact, project dates)

### Requirement 2: Assessment Data Ingestion

**User Story:** As a migration consultant, I want to import assessment data from multiple sources, so that I can have a complete view of the client's infrastructure.

#### Acceptance Criteria

1. WHEN a user imports RVTools export files THEN the Parser SHALL extract VM information and store it in normalized format within the Client_Workspace
2. WHEN a user imports Cloudamize Observed Infrastructure files THEN the Parser SHALL extract compute, storage, and network data in normalized format
3. WHEN a user imports Cloudamize Migration Planner files THEN the Parser SHALL extract application mappings and migration wave assignments
4. IF an import file has invalid format THEN the Stack_Sense_Core SHALL return a descriptive error indicating the expected format
5. WHEN data is imported from multiple sources THEN the Stack_Sense_Core SHALL correlate servers by hostname or IP to create unified records
6. THE Parser SHALL produce normalized JSON output that can be serialized and deserialized without data loss (round-trip property)

### Requirement 3: Infrastructure Analysis Engine

**User Story:** As a migration consultant, I want to analyze the client's infrastructure automatically, so that I can generate AWS recommendations efficiently.

#### Acceptance Criteria

1. WHEN analysis is triggered THEN the Analyzer SHALL process all normalized assessment data and generate EC2 instance recommendations
2. WHEN analysis is triggered THEN the Analyzer SHALL calculate total resource requirements (vCPUs, memory, storage)
3. WHEN analysis is triggered THEN the Analyzer SHALL identify application dependencies and groupings
4. THE Analyzer SHALL generate cost estimates using AWS Pricing API for recommended resources
5. WHEN analysis completes THEN the Stack_Sense_Core SHALL persist results in the Client_Workspace analysis directory
6. IF assessment data is incomplete THEN the Analyzer SHALL flag missing data and proceed with available information

### Requirement 4: Application Analysis Output

**User Story:** As a migration consultant, I want each analyzed application to generate a detailed output file, so that I can track and refine application-specific migration details over time.

#### Acceptance Criteria

1. WHEN an application is analyzed THEN the Analyzer SHALL generate a dedicated JSON file with all application details in the Client_Workspace
2. WHEN an application output file is generated THEN it SHALL include: application name, servers involved, dependencies, recommended AWS services, estimated costs, and migration strategy (7R)
3. WHEN an application output file is generated THEN it SHALL include a Markdown summary suitable for documentation
4. THE Analyzer SHALL update existing application files when re-analysis is performed, preserving manual annotations
5. WHEN listing applications THEN the Stack_Sense_Core SHALL read from generated application files to display current state
6. THE application output format SHALL support round-trip serialization (JSON to object to JSON produces equivalent output)
7. WHEN an application file is modified manually THEN the Stack_Sense_Core SHALL validate the structure before accepting changes

### Requirement 5: Migration Wave Planning

**User Story:** As a migration consultant, I want to define and manage migration waves, so that I can plan phased migrations for the client.

#### Acceptance Criteria

1. WHEN a user creates a migration wave THEN the Stack_Sense_Core SHALL allow assignment of applications and servers to that wave
2. WHEN a migration wave is defined THEN the Stack_Sense_Core SHALL calculate wave-specific resource requirements and costs
3. WHEN viewing migration waves THEN the Stack_Sense_Core SHALL display dependencies between waves
4. THE Stack_Sense_Core SHALL validate that wave assignments respect application dependencies
5. WHEN a wave is modified THEN the Stack_Sense_Core SHALL recalculate affected metrics automatically

### Requirement 6: Business Case Generation

**User Story:** As a migration consultant, I want to generate business case documents, so that I can present migration justification to stakeholders.

#### Acceptance Criteria

1. WHEN a user requests a business case THEN the Stack_Sense_Core SHALL generate a document with cost comparison (on-premise vs AWS)
2. WHEN generating business case THEN the Stack_Sense_Core SHALL include ROI calculations based on defined parameters
3. WHEN generating business case THEN the Stack_Sense_Core SHALL include migration timeline based on wave definitions
4. THE Stack_Sense_Core SHALL export business case in Markdown format
5. WHEN business case is generated THEN the Stack_Sense_Core SHALL include all referenced diagrams and charts

### Requirement 7: Architecture Diagram Generation

**User Story:** As a migration consultant, I want to generate architecture diagrams automatically, so that I can visualize current and target states.

#### Acceptance Criteria

1. WHEN a user requests current state diagram THEN the Stack_Sense_Core SHALL generate a diagram showing on-premise infrastructure
2. WHEN a user requests target state diagram THEN the Stack_Sense_Core SHALL generate AWS architecture diagram with recommended services
3. WHEN a user requests migration flow diagram THEN the Stack_Sense_Core SHALL generate a diagram showing the migration sequence
4. THE Stack_Sense_Core SHALL save generated diagrams in PNG format within the Client_Workspace diagrams directory
5. WHEN diagrams are generated THEN the Stack_Sense_Core SHALL use consistent styling and AWS iconography

### Requirement 8: Presentation Layer

**User Story:** As a migration consultant, I want a web interface to present analysis results, so that I can share findings with clients interactively.

#### Acceptance Criteria

1. WHEN the Presentation_App loads THEN it SHALL display a list of available client workspaces
2. WHEN a user selects a client THEN the Presentation_App SHALL display the executive summary dashboard
3. WHEN viewing a client THEN the Presentation_App SHALL show infrastructure inventory with filtering and search
4. WHEN viewing a client THEN the Presentation_App SHALL display migration waves with timeline visualization
5. WHEN viewing a client THEN the Presentation_App SHALL show cost analysis with interactive charts
6. WHEN viewing a client THEN the Presentation_App SHALL display architecture diagrams with zoom and pan capabilities
7. THE Presentation_App SHALL load data from Client_Workspace JSON files without requiring a backend server

### Requirement 9: Project Structure Reorganization

**User Story:** As a developer, I want a clean project structure, so that I can maintain and extend Stack Sense efficiently.

#### Acceptance Criteria

1. THE Stack_Sense_Core SHALL organize source code in a `src/` directory with subdirectories for parsers, analyzers, and generators
2. THE Stack_Sense_Core SHALL store client workspaces in a `clients/` directory at project root
3. THE Presentation_App SHALL be contained in a `presentation/` directory with its own build configuration
4. THE Stack_Sense_Core SHALL provide a CLI interface for all core operations
5. WHEN the project is cloned THEN a developer SHALL be able to set up the environment with a single command
6. THE Stack_Sense_Core SHALL maintain backward compatibility with existing BGR data during migration

