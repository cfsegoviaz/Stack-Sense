import React, { useState } from 'react';
import { 
  PieChart, 
  TrendingDown, 
  Server, 
  Database, 
  Cloud, 
  ArrowRight, 
  DollarSign, 
  CheckCircle, 
  AlertTriangle,
  BarChart3,
  Cpu,
  ShieldCheck,
  Globe
} from 'lucide-react';

const appsData = [
  {
    id: 'api-portal',
    name: 'Api Portal',
    strategy: 'Refactor (Serverless)',
    migrationType: 'Static Site Hosting',
    icon: Globe,
    currentCost: 2000,
    targetCost: 1.50,
    savingsPercent: 99.9,
    description: 'Transformación de 5 VMs Windows pesadas a una arquitectura puramente estática y serverless.',
    fromStack: ['5 VMs Windows', '42 vCPUs', '144GB RAM'],
    toStack: ['AWS Amplify', 'S3 + CloudFront', 'Azure DevOps'],
    architecture: [
      { step: 'DevOps', desc: 'Azure Pipelines' },
      { step: 'Hosting', desc: 'S3 + CloudFront' },
      { step: 'Security', desc: 'Cert Manager (SSL Gratis)' }
    ],
    insight: 'El caso de éxito financiero más impactante. Se elimina completamente el mantenimiento de SO y licencias.'
  },
  {
    id: 'saras',
    name: 'SARAS',
    strategy: 'Replatform (Containerization)',
    migrationType: 'ECS + Babelfish',
    icon: Server,
    currentCost: 1400,
    targetCost: 904,
    savingsPercent: 35,
    description: 'Modernización a contenedores y eliminación de licencia SQL Server usando compatibilidad Babelfish.',
    fromStack: ['2 VMs Windows', 'SQL Server', 'Monolito'],
    toStack: ['ECS Fargate', 'Aurora Babelfish (PostgreSQL)', 'Redis'],
    architecture: [
      { step: 'Compute', desc: 'ECS Fargate (Auto-scaling)' },
      { step: 'Database', desc: 'Aurora PostgreSQL + Babelfish' },
      { step: 'Cache', desc: 'ElastiCache Redis' }
    ],
    insight: 'Babelfish es la clave aquí: permite usar PostgreSQL sin reescribir el código T-SQL existente, ahorrando meses de desarrollo.'
  },
  {
    id: 'sonarqube',
    name: 'SonarQube',
    strategy: 'Replatform (Optimized)',
    migrationType: 'Lift & Shift Optimizado',
    icon: CheckCircle,
    currentCost: 1500,
    targetCost: 404,
    savingsPercent: 73,
    description: 'Consolidación de infraestructura y cambio de motor de base de datos a Open Source.',
    fromStack: ['3 VMs Windows', 'SQL Server', 'Infra dispersa'],
    toStack: ['1 EC2 Linux (Rightsized)', 'RDS PostgreSQL', 'EFS'],
    architecture: [
      { step: 'Compute', desc: 'EC2 t3.xlarge (Linux)' },
      { step: 'Database', desc: 'RDS PostgreSQL Multi-AZ' },
      { step: 'Storage', desc: 'EFS (Shared Plugins)' }
    ],
    insight: 'Pasar de Windows a Linux y de SQL Server a Postgres elimina costos de licencia y reduce overhead de recursos.'
  },
  {
    id: 'backoffice',
    name: 'Backoffice Sistemas',
    strategy: 'Rehost (Hybrid)',
    migrationType: 'Lift & Shift Híbrido',
    icon: Cloud,
    currentCost: 0, // No explicit current cost in doc, but implies high overhead
    targetCost: 402,
    isHybrid: true,
    description: 'Migración de capa aplicativa a la nube manteniendo datos on-premise mediante VPN segura.',
    fromStack: ['On-Premise Datacenter', 'Conectividad Local'],
    toStack: ['EC2 Windows', 'Site-to-Site VPN', 'SQL Server On-Prem'],
    architecture: [
      { step: 'Web Tier', desc: 'EC2 Windows + ALB' },
      { step: 'Network', desc: 'VPN Site-to-Site (AES-256)' },
      { step: 'Data Tier', desc: 'SQL Server On-Premise (Legacy)' }
    ],
    insight: 'Estrategia de menor riesgo. Permite ganar escalabilidad en la web sin enfrentar la complejidad de migrar la BD data legacy inmediatamente.'
  },
  {
    id: 'seq',
    name: 'Seq (Logs)',
    strategy: 'Refactor (Native)',
    migrationType: 'Modernización a CloudWatch',
    icon: BarChart3,
    currentCost: 1833, // Approx monthly from $22k/yr
    targetCost: 278,
    savingsPercent: 85,
    description: 'Reemplazo de herramienta propietaria por servicios nativos de observabilidad de AWS.',
    fromStack: ['3 Windows Servers', 'SQL Server Enterprise', 'Monolito .NET'],
    toStack: ['CloudWatch Logs', 'OpenSearch', 'Lambda'],
    architecture: [
      { step: 'Ingest', desc: 'CloudWatch Agent' },
      { step: 'Search', desc: 'OpenSearch Service' },
      { step: 'Archival', desc: 'S3 Glacier' }
    ],
    insight: 'Elimina un punto único de fallo y costos masivos de licenciamiento Enterprise. Pasa a un modelo "Pay-as-you-go".'
  }
];

const CostBar = ({ current, target, percent, isHybrid }) => {
  const max = Math.max(current, target || 0) * 1.1;
  
  if (isHybrid) {
    return (
      <div className="mt-4 p-4 bg-amber-50 rounded-lg border border-amber-200">
        <div className="flex items-center text-amber-800 font-semibold mb-2">
          <AlertTriangle className="w-4 h-4 mr-2" />
          Modelo Híbrido - Costo Mixto
        </div>
        <p className="text-sm text-amber-700">
          Costo AWS: <strong>${target}/mes</strong> + Costo On-Premise (Licencias SQL Server existentes).
          <br/>
          <em>El ahorro vendrá en la Fase 3 con la migración a Babelfish.</em>
        </p>
      </div>
    );
  }

  return (
    <div className="mt-6 space-y-3">
      <div className="flex justify-between text-sm font-medium text-slate-600">
        <span>Costo Actual (Aprox)</span>
        <span>Meta AWS</span>
      </div>
      <div className="relative h-12 bg-slate-100 rounded-full overflow-hidden flex">
        {/* Current Cost Background Bar */}
        <div className="absolute top-0 left-0 h-full bg-slate-200 w-full rounded-full"></div>
        
        {/* Target Cost Bar */}
        <div 
          className="relative h-full bg-emerald-500 flex items-center justify-end px-3 text-white font-bold transition-all duration-1000"
          style={{ width: `${(target / current) * 100}%`, minWidth: '80px' }}
        >
          ${target}
        </div>
        
        {/* Savings Marker */}
        <div className="absolute top-0 right-4 h-full flex items-center text-slate-500 text-xs">
          AHORRO: {percent}%
        </div>
      </div>
      <div className="text-xs text-slate-400 text-right">
        De ${current}/mes a ${target}/mes
      </div>
    </div>
  );
};

export default function BGRMigrationDashboard() {
  const [selectedApp, setSelectedApp] = useState(appsData[0]);

  // Calculations for summary
  const totalCurrentEstimated = 2000 + 1400 + 1500 + 1833; // Excluding hybrid
  const totalTarget = 1.5 + 904 + 404 + 278; // Excluding hybrid AWS cost only
  const totalSavings = totalCurrentEstimated - totalTarget;

  return (
    <div className="min-h-screen bg-slate-50 p-6 font-sans text-slate-800">
      
      {/* Header */}
      <header className="mb-8">
        <div className="flex items-center space-x-3 mb-2">
          <Cloud className="w-8 h-8 text-blue-600" />
          <h1 className="text-2xl font-bold text-slate-900">BGR Cloud Migration Strategy</h1>
        </div>
        <p className="text-slate-500">Análisis de Arquitectura Objetivo y ROI para Banco General Rumiñahui</p>
      </header>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-semibold text-slate-500 uppercase">Ahorro Mensual Potencial</h3>
            <TrendingDown className="w-5 h-5 text-emerald-500" />
          </div>
          <div className="text-3xl font-bold text-slate-900">
            ${totalSavings.toLocaleString('en-US', { maximumFractionDigits: 0 })}
            <span className="text-sm font-normal text-emerald-600 ml-2">/ mes</span>
          </div>
          <p className="text-xs text-slate-400 mt-2">Aprox. $50k anuales en solo 4 aplicaciones</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-semibold text-slate-500 uppercase">Estrategia Dominante</h3>
            <Cpu className="w-5 h-5 text-blue-500" />
          </div>
          <div className="text-2xl font-bold text-slate-900">Modernización</div>
          <p className="text-xs text-slate-400 mt-2">Containerización & Serverless sobre Lift & Shift puro</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-semibold text-slate-500 uppercase">Tecnología Clave</h3>
            <Database className="w-5 h-5 text-indigo-500" />
          </div>
          <div className="text-2xl font-bold text-slate-900">Aurora Babelfish</div>
          <p className="text-xs text-slate-400 mt-2">Migración de SQL Server a Postgres sin cambios de código</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Sidebar Navigation */}
        <div className="lg:col-span-4 space-y-4">
          <h3 className="font-semibold text-slate-700 px-2">Aplicaciones Analizadas</h3>
          {appsData.map((app) => (
            <button
              key={app.id}
              onClick={() => setSelectedApp(app)}
              className={`w-full text-left p-4 rounded-lg transition-all border ${
                selectedApp.id === app.id 
                  ? 'bg-white border-blue-500 ring-1 ring-blue-500 shadow-md' 
                  : 'bg-white border-slate-200 hover:border-blue-300 hover:bg-slate-50'
              }`}
            >
              <div className="flex items-start justify-between">
                <div className="flex items-center space-x-3">
                  <div className={`p-2 rounded-lg ${selectedApp.id === app.id ? 'bg-blue-100 text-blue-600' : 'bg-slate-100 text-slate-500'}`}>
                    <app.icon className="w-5 h-5" />
                  </div>
                  <div>
                    <h4 className="font-bold text-slate-800">{app.name}</h4>
                    <span className="text-xs font-medium text-slate-500 px-2 py-0.5 bg-slate-100 rounded-full">
                      {app.migrationType}
                    </span>
                  </div>
                </div>
                {app.savingsPercent && (
                  <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded">
                    -{app.savingsPercent}% Costo
                  </span>
                )}
              </div>
            </button>
          ))}
        </div>

        {/* Detail View */}
        <div className="lg:col-span-8">
          <div className="bg-white rounded-xl shadow-lg border border-slate-200 overflow-hidden">
            
            {/* Detail Header */}
            <div className="p-6 border-b border-slate-100 bg-slate-50/50">
              <div className="flex justify-between items-start">
                <div>
                  <h2 className="text-2xl font-bold text-slate-800 flex items-center">
                    {selectedApp.name}
                    <span className="ml-3 text-sm font-normal text-white bg-slate-800 px-3 py-1 rounded-full">
                      {selectedApp.strategy}
                    </span>
                  </h2>
                  <p className="mt-2 text-slate-600">{selectedApp.description}</p>
                </div>
              </div>
            </div>

            {/* Content Body */}
            <div className="p-6 space-y-8">
              
              {/* Architecture Transformation */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="space-y-3">
                  <h4 className="text-sm font-bold text-slate-400 uppercase tracking-wider">Estado Actual (Legacy)</h4>
                  <ul className="space-y-2">
                    {selectedApp.fromStack.map((item, i) => (
                      <li key={i} className="flex items-center text-red-700 bg-red-50 p-2 rounded border border-red-100 text-sm">
                        <Server className="w-4 h-4 mr-2 opacity-60" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="flex flex-col items-center justify-center md:hidden">
                  <ArrowRight className="w-6 h-6 text-slate-300 rotate-90" />
                </div>

                <div className="space-y-3">
                  <h4 className="text-sm font-bold text-emerald-600 uppercase tracking-wider">Arquitectura Objetivo AWS</h4>
                  <ul className="space-y-2">
                    {selectedApp.toStack.map((item, i) => (
                      <li key={i} className="flex items-center text-emerald-800 bg-emerald-50 p-2 rounded border border-emerald-100 text-sm font-medium">
                        <CheckCircle className="w-4 h-4 mr-2 text-emerald-500" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              {/* Financial Analysis */}
              <div className="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 className="font-bold text-slate-800 mb-2 flex items-center">
                  <DollarSign className="w-5 h-5 mr-2 text-green-600" />
                  Impacto Financiero
                </h3>
                <CostBar 
                  current={selectedApp.currentCost} 
                  target={selectedApp.targetCost} 
                  percent={selectedApp.savingsPercent} 
                  isHybrid={selectedApp.isHybrid}
                />
              </div>

              {/* Architect's Insight */}
              <div className="bg-blue-50 p-5 rounded-xl border border-blue-100">
                <h3 className="text-sm font-bold text-blue-800 mb-2 flex items-center uppercase">
                  <ShieldCheck className="w-4 h-4 mr-2" />
                  Opinión del Arquitecto
                </h3>
                <p className="text-blue-900 text-sm leading-relaxed">
                  {selectedApp.insight}
                </p>
                
                {/* Visual Flow Representation */}
                <div className="mt-6 pt-4 border-t border-blue-200">
                   <div className="flex items-center justify-between text-xs text-blue-700 font-mono">
                      {selectedApp.architecture.map((node, i) => (
                        <React.Fragment key={i}>
                          <div className="flex flex-col items-center text-center max-w-[80px]">
                            <div className="w-8 h-8 rounded-lg bg-blue-200 flex items-center justify-center mb-2 shadow-sm">
                              {i + 1}
                            </div>
                            <span className="font-bold">{node.step}</span>
                            <span className="opacity-75 text-[10px]">{node.desc}</span>
                          </div>
                          {i < selectedApp.architecture.length - 1 && (
                            <div className="h-0.5 flex-1 bg-blue-300 mx-2"></div>
                          )}
                        </React.Fragment>
                      ))}
                   </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}