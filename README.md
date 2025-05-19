# agent-networking-ai

Agente de Inteligencia Artificial para automatización y análisis de redes.

## Descripción
Este proyecto integra Nornir y modelos de OpenAI (a través del framework Agno) para crear un agente conversacional que consulta dispositivos de red en tiempo real, recoge datos (ARP, BGP, interfaces, VLANs, etc.) y responde consultas en lenguaje natural presentando la información en tablas Markdown agrupadas por dispositivo.

## Características
- Recolección de datos de red mediante Nornir y plugins (NAPALM, Napalm, Netmiko).
- Soporte para ARP, BGP (vecinos y configuración), interfaces, VLANs, ACLs, LLDP, SNMP, NTP, y más.
- Procesamiento y parseo automático de JSON en los resultados de Nornir.
- Interfaz de línea de comandos interactiva basada en Agno Agent (OpenAIChat).

## Requisitos
- Python 3.8+
- Variable de entorno `OPENAI_API_KEY` configurada con tu clave de OpenAI.
- Dependencias del proyecto (instalables con pip):
  ```bash
  pip install -r requirements.txt
  ```

## Instalación
```bash
git clone <repositorio>
cd agent-networking-ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración
1. Define tu inventario de dispositivos en `inventory/hosts.yaml`.
2. Ajusta la configuración de Nornir en `config.yaml` (número de trabajadores, plugins, etc.).
3. (Opcional) Personaliza `inventory/groups.yaml` y `inventory/defaults.yaml` para variables de entorno y credenciales por defecto.
4. Exporta tu clave de OpenAI:
   ```bash
   export OPENAI_API_KEY="tu_api_key"
   ```

## Estructura del proyecto
- `main.py`: punto de entrada; lanza la CLI del agente.
- `config.yaml` y `inventory/`: configuración de Nornir e inventario de dispositivos.
- `src/agents.py`: definición y configuración del agente Agno.
- `src/nornir_network_inventory.py`: inicializa Nornir con la configuración definida.
- `src/result_processor.py`: parsea los resultados de Nornir y extrae JSON.
- `src/network_data/`: módulos que implementan funciones de recolección de datos específicos (fact, interfaces, BGP, etc.).
- `requirements.txt`: dependencias del proyecto.

## Uso
Activa el entorno virtual y ejecuta:
```bash
python main.py
```
En la interfaz interactiva, ingresa consultas en lenguaje natural. Por ejemplo:
```
> Muéstrame los vecinos BGP de todos los dispositivos
```
El agente recopilará los datos necesarios y mostrará tablas Markdown por dispositivo.

## Contribuciones
Pull requests y reportes de issues son bienvenidos. ¡Toda colaboración es apreciada!