# API Documentation

## Overview
The Censys Data Summarizer provides a REST API for analyzing security host data using AI-powered summarization.

## Base URL
```
http://localhost:5000
```

## Endpoints

### POST /summarize
Analyzes Censys host data and returns a structured security summary.

#### Request
**Content-Type:** `application/json`

**Body:**
```json
{
  "hosts": [
    {
      "ip": "192.168.1.1",
      "location": {
        "country": "United States",
        "city": "New York",
        "country_code": "US"
      },
      "autonomous_system": {
        "asn": 12345,
        "name": "Example ISP",
        "country_code": "US"
      },
      "services": [
        {
          "port": 22,
          "protocol": "SSH",
          "banner": "SSH-2.0-OpenSSH_8.2",
          "software": [
            {
              "product": "openssh",
              "vendor": "openbsd",
              "version": "8.2"
            }
          ],
          "vulnerabilities": [
            {
              "cve_id": "CVE-2023-1234",
              "severity": "critical",
              "cvss_score": 9.8,
              "description": "Remote code execution vulnerability"
            }
          ]
        }
      ],
      "threat_intelligence": {
        "risk_level": "high",
        "security_labels": ["REMOTE_ACCESS"],
        "malware_detected": {
          "name": "Example Malware",
          "type": "trojan",
          "confidence": 0.85
        }
      }
    }
  ]
}
```

#### Response
**Status Code:** `200 OK`

**Content-Type:** `application/json`

```json
{
  "metrics": {
    "total_hosts": 1,
    "critical_risk": 0,
    "high_risk": 1,
    "services_count": 1,
    "unique_vulnerabilities": 1,
    "countries": ["United States"]
  },
  "summary": "# Executive Summary\n\nThis analysis covers 1 IP address with significant security risks...\n\n## Quick Metrics\n\n- Total Hosts: 1\n- Critical Risk: 0\n- High Risk: 1\n- Services: 1\n- Unique Vulnerabilities: 1\n- Countries: United States\n\n## Overall Risk Assessment\n\n...",
  "hosts_count": 1
}
```

#### Error Responses

**400 Bad Request**
```json
{
  "error": "Invalid data format. Expected 'hosts' array."
}
```

**500 Internal Server Error**
```json
{
  "error": "Processing error: API request failed"
}
```

### GET /
Returns the main web interface.

#### Response
**Status Code:** `200 OK`

**Content-Type:** `text/html`

Returns the HTML page for the web interface.

## Data Models

### Host Object
```json
{
  "ip": "string (required)",
  "location": {
    "country": "string",
    "city": "string", 
    "country_code": "string",
    "coordinates": {
      "latitude": "number",
      "longitude": "number"
    }
  },
  "autonomous_system": {
    "asn": "number",
    "name": "string",
    "country_code": "string"
  },
  "dns": {
    "hostname": "string"
  },
  "operating_system": {
    "vendor": "string",
    "product": "string"
  },
  "services": [
    {
      "port": "number",
      "protocol": "string",
      "banner": "string",
      "software": [
        {
          "product": "string",
          "vendor": "string", 
          "version": "string"
        }
      ],
      "vulnerabilities": [
        {
          "cve_id": "string",
          "severity": "string (critical|high|medium|low)",
          "cvss_score": "number",
          "description": "string"
        }
      ],
      "malware_detected": {
        "name": "string",
        "type": "string",
        "confidence": "number (0-1)",
        "threat_actors": ["string"]
      }
    }
  ],
  "threat_intelligence": {
    "risk_level": "string (critical|high|medium|low)",
    "security_labels": ["string"],
    "malware_families": ["string"]
  }
}
```

### Metrics Object
```json
{
  "total_hosts": "number",
  "critical_risk": "number", 
  "high_risk": "number",
  "services_count": "number",
  "unique_vulnerabilities": "number",
  "countries": ["string"]
}
```

## Rate Limiting
- No rate limiting currently implemented
- Consider implementing for production use

## Authentication
- No authentication currently required
- API key is server-side only

## Error Codes
- `400` - Bad Request (invalid JSON, missing required fields)
- `500` - Internal Server Error (API failures, processing errors)

## Example Usage

### cURL
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d @sample_data.json
```

### Python
```python
import requests
import json

url = "http://localhost:5000/summarize"
data = {
    "hosts": [
        {
            "ip": "192.168.1.1",
            "threat_intelligence": {"risk_level": "high"},
            "services": []
        }
    ]
}

response = requests.post(url, json=data)
result = response.json()
print(result["summary"])
```

### JavaScript
```javascript
const response = await fetch('http://localhost:5000/summarize', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        hosts: [
            {
                ip: "192.168.1.1",
                threat_intelligence: { risk_level: "high" },
                services: []
            }
        ]
    })
});

const result = await response.json();
console.log(result.summary);
```
