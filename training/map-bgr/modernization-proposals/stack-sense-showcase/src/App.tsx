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
  Globe,
  Star
} from 'lucide-react';

const appsData = [
  {
    id: 'api-portal',
    name: 'Api Portal',
    icon: Globe,
    currentCost: 2000,
    strategies: [
      {
        id: 'refactor',
        name: 'Refactor (Serverless)',
        recommended: true,
        migrationType: 'Static Site Hosting',
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
        insight: 'El caso de éxito financiero más impactante. Se elimina completamente el mantenimiento de SO y licencias.',
        diagram: '/diagrams/app_apiportal.png'
      }
    ]
  },
  {
    id: 'saras',
    name: 'SARAS',
    icon: Server,
    currentCost: 1400,
    strategies: [
      {
        id: 'replatform',
        name: 'Replatform (Containerization)',
        recommended: true,
        migrationType: 'ECS + Babelfish',
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
        insight: 'Babelfish es la clave aquí: permite usar PostgreSQL sin reescribir el código T-SQL existente, ahorrando meses de desarrollo.',
        diagram: '/diagrams/app_saras.png'
      }
    ]
  },
  {
    id: 'sonarqube',
    name: 'SonarQube',
    icon: CheckCircle,
    currentCost: 1500,
    strategies: [
      {
        id: 'replatform',
        name: 'Replatform (Optimized)',
        recommended: true,
        migrationType: 'Lift & Shift Optimizado',
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
        insight: 'Pasar de Windows a Linux y de SQL Server a Postgres elimina costos de licencia y reduce overhead de recursos.',
        diagram: '/diagrams/arch_sonarqube.png'
      }
    ]
  },
  {
    id: 'backoffice',
    name: 'Backoffice Sistemas',
    icon: Cloud,
    currentCost: 0,
    strategies: [
      {
        id: 'hybrid',
        name: 'Rehost (Hybrid)',
        recommended: true,
        migrationType: 'Lift & Shift Híbrido',
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
        insight: 'Estrategia de menor riesgo. Permite ganar escalabilidad en la web sin enfrentar la complejidad de migrar la BD data legacy inmediatamente.',
        diagram: '/diagrams/app_backoffice_sistemas.png'
      }
    ]
  },
  {
    id: 'seq',
    name: 'Seq (Logs)',
    icon: BarChart3,
    currentCost: 1833,
    strategies: [
      {
        id: 'refactor-native',
        name: 'Modernización Completa',
        recommended: true,
        migrationType: 'Servicios AWS Nativos',
        targetCost: 278,
        savingsPercent: 85,
        description: 'Reemplazo completo con servicios AWS nativos: CloudWatch Logs + OpenSearch Service para análisis avanzado.',
        fromStack: ['3 Windows Servers', 'SQL Server Enterprise', 'Seq Monolito'],
        toStack: ['CloudWatch Logs', 'OpenSearch Service', 'Lambda', 'S3 Glacier', 'SNS'],
        architecture: [
          { step: 'Ingest', desc: 'CloudWatch Agent' },
          { step: 'Storage', desc: 'CloudWatch Logs' },
          { step: 'Search', desc: 'OpenSearch Service' },
          { step: 'Archival', desc: 'S3 Glacier' }
        ],
        insight: 'Elimina licencias SQL Server Enterprise (~$14k/año) y Windows Server. Servicios nativos AWS con mejor integración, escalabilidad automática y modelo pay-as-you-go. Ahorro de $18,664/año (85%).',
        diagram: '/diagrams/arch_seq_cloudwatch.png'
      },
      {
        id: 'rehost',
        name: 'Lift & Shift',
        recommended: false,
        migrationType: 'Rehost EC2',
        targetCost: 129,
        savingsPercent: 93,
        description: 'Migración directa de Seq a EC2 Linux + RDS PostgreSQL manteniendo la aplicación original.',
        fromStack: ['3 Windows Servers', 'SQL Server Enterprise', 'Seq Monolito'],
        toStack: ['EC2 Linux (t3.medium)', 'RDS PostgreSQL', 'EFS', 'ALB', 'S3 Backups'],
        architecture: [
          { step: 'Compute', desc: 'EC2 t3.medium' },
          { step: 'Database', desc: 'RDS PostgreSQL' },
          { step: 'Storage', desc: 'EFS' },
          { step: 'Load Balancer', desc: 'ALB' }
        ],
        insight: 'NO RECOMENDADA: Aunque tiene mayor ahorro ($20,452/año - 93%), Seq duplica funcionalidad AWS nativa. Requiere gestión de infraestructura, actualizaciones y menor integración con ecosistema AWS.',
        diagram: '/diagrams/arch_seq_ec2.png'
      }
    ]
  }
];

const CostBar = ({ current, target, percent, isHybrid }: any) => {
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
        <div className="absolute top-0 left-0 h-full bg-slate-200 w-full rounded-full"></div>
        
        <div 
          className="relative h-full bg-emerald-500 flex items-center justify-end px-3 text-white font-bold transition-all duration-1000"
          style={{ width: `${(target / current) * 100}%`, minWidth: '80px' }}
        >
          ${target}
        </div>
        
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
  const [selectedStrategy, setSelectedStrategy] = useState(appsData[0].strategies[0]);

  const totalCurrentEstimated = 2000 + 1400 + 1500 + 1833;
  const totalTarget = 1.5 + 904 + 404 + 278;
  const totalSavings = totalCurrentEstimated - totalTarget;

  const handleAppChange = (app: any) => {
    setSelectedApp(app);
    setSelectedStrategy(app.strategies[0]);
  };

  return (
    <div className="min-h-screen bg-slate-50 p-6 font-sans text-slate-800">
      
      <header className="mb-8">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <img src="/logo.png" alt="BGR Logo" className="w-16 h-16 object-contain" />
            <div>
              <h1 className="text-2xl font-bold text-slate-900">BGR Cloud Migration Strategy</h1>
              <p className="text-slate-500">Análisis de Arquitectura Objetivo y ROI para Banco General Rumiñahui</p>
            </div>
          </div>
          <div className="text-right">
            <div className="text-sm font-semibold text-slate-700">Arquitecto Asignado</div>
            <div className="text-lg font-bold text-blue-600">Christian Segovia</div>
            <div className="text-xs text-slate-600 space-y-0.5 mt-1">
              <div>📞 +593 960224059</div>
              <div>✉️ christian.segovia@escala24x7.com</div>
            </div>
          </div>
        </div>
      </header>

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

      <div className="flex gap-8">
        
        {/* Sidebar fijo a la izquierda */}
        <div className="w-80 flex-shrink-0 sticky top-6 self-start space-y-4">
          <h3 className="font-semibold text-slate-700 px-2">Aplicaciones Analizadas</h3>
          {appsData.map((app) => (
            <button
              key={app.id}
              onClick={() => handleAppChange(app)}
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
                      {app.strategies.length} {app.strategies.length === 1 ? 'Estrategia' : 'Estrategias'}
                    </span>
                  </div>
                </div>
                {app.strategies[0].savingsPercent && (
                  <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded">
                    -{app.strategies[0].savingsPercent}% Costo
                  </span>
                )}
              </div>
            </button>
          ))}
        </div>

        {/* Contenido principal */}
        <div className="flex-1 min-w-0">
          {/* Pestañas de Estrategias - Fuera de la card */}
          {selectedApp.strategies.length > 1 && (
            <div className="mb-4 bg-white rounded-lg shadow-sm border border-slate-200 p-2">
              <div className="flex gap-2">
                {selectedApp.strategies.map((strategy: any) => (
                  <button
                    key={strategy.id}
                    onClick={() => setSelectedStrategy(strategy)}
                    className={`flex-1 px-4 py-3 rounded-md font-semibold text-sm transition-all ${
                      selectedStrategy.id === strategy.id
                        ? 'bg-blue-600 text-white shadow-md'
                        : 'bg-slate-50 text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <div className="flex items-center justify-center gap-2">
                      <span>{strategy.name}</span>
                      {strategy.recommended && (
                        <Star className="w-4 h-4 fill-yellow-300 text-yellow-300" />
                      )}
                    </div>
                    {selectedStrategy.id === strategy.id && (
                      <div className="text-xs mt-1 opacity-90">
                        ${strategy.targetCost}/mes · {strategy.savingsPercent}% ahorro
                      </div>
                    )}
                  </button>
                ))}
              </div>
            </div>
          )}

          <div className="bg-white rounded-xl shadow-lg border border-slate-200 overflow-hidden">
            
            <div className="p-6 border-b border-slate-100 bg-slate-50/50">
              <div className="flex justify-between items-start">
                <div>
                  <h2 className="text-2xl font-bold text-slate-800">{selectedApp.name}</h2>
                  <div className="mt-3 flex items-center gap-2">
                    <span className="text-sm font-medium text-slate-600 bg-white px-3 py-1 rounded-full border border-slate-200">
                      {selectedStrategy.migrationType}
                    </span>
                    {selectedStrategy.recommended && (
                      <span className="text-xs bg-green-100 text-green-800 px-2 py-1 rounded-full font-semibold">
                        ✓ RECOMENDADA
                      </span>
                    )}
                    {selectedStrategy.recommended === false && (
                      <span className="text-xs bg-red-100 text-red-800 px-2 py-1 rounded-full font-semibold">
                        ⚠ NO RECOMENDADA
                      </span>
                    )}
                  </div>
                </div>
              </div>
              <p className="mt-3 text-slate-600">{selectedStrategy.description}</p>
            </div>

            <div className="p-6 space-y-8">
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="space-y-3">
                  <h4 className="text-sm font-bold text-slate-400 uppercase tracking-wider">Estado Actual (Legacy)</h4>
                  <ul className="space-y-2">
                    {selectedStrategy.fromStack.map((item: string, i: number) => (
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
                    {selectedStrategy.toStack.map((item: string, i: number) => (
                      <li key={i} className="flex items-center text-emerald-800 bg-emerald-50 p-2 rounded border border-emerald-100 text-sm font-medium">
                        <CheckCircle className="w-4 h-4 mr-2 text-emerald-500" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              <div className="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 className="font-bold text-slate-800 mb-2 flex items-center">
                  <DollarSign className="w-5 h-5 mr-2 text-green-600" />
                  Impacto Financiero
                </h3>
                <CostBar 
                  current={selectedApp.currentCost} 
                  target={selectedStrategy.targetCost} 
                  percent={selectedStrategy.savingsPercent} 
                  isHybrid={selectedStrategy.isHybrid}
                />
              </div>

              <div className="bg-blue-50 p-5 rounded-xl border border-blue-100">
                <h3 className="text-sm font-bold text-blue-800 mb-2 flex items-center uppercase">
                  <ShieldCheck className="w-4 h-4 mr-2" />
                  Recomendación Técnica Escala24x7
                </h3>
                <p className="text-blue-900 text-sm leading-relaxed">
                  {selectedStrategy.insight}
                </p>
                
                <div className="mt-6 pt-4 border-t border-blue-200">
                   <div className="flex items-center justify-between text-xs text-blue-700 font-mono">
                      {selectedStrategy.architecture.map((node: any, i: number) => (
                        <React.Fragment key={i}>
                          <div className="flex flex-col items-center text-center max-w-[80px]">
                            <div className="w-8 h-8 rounded-lg bg-blue-200 flex items-center justify-center mb-2 shadow-sm">
                              {i + 1}
                            </div>
                            <span className="font-bold">{node.step}</span>
                            <span className="opacity-75 text-[10px]">{node.desc}</span>
                          </div>
                          {i < selectedStrategy.architecture.length - 1 && (
                            <div className="h-0.5 flex-1 bg-blue-300 mx-2"></div>
                          )}
                        </React.Fragment>
                      ))}
                   </div>
                </div>
              </div>

              {selectedStrategy.diagram && (
                <div className="bg-white p-6 rounded-xl border border-slate-200">
                  <h3 className="text-sm font-bold text-slate-700 mb-4 flex items-center uppercase">
                    <BarChart3 className="w-4 h-4 mr-2" />
                    Diagrama de Arquitectura - {selectedStrategy.name}
                  </h3>
                  <div className="bg-slate-50 rounded-lg p-4 border border-slate-200">
                    <img 
                      src={selectedStrategy.diagram} 
                      alt={`Arquitectura de ${selectedApp.name} - ${selectedStrategy.name}`}
                      className="w-full h-auto rounded-lg shadow-sm"
                    />
                  </div>
                </div>
              )}

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
