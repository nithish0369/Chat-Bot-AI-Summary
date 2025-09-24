# Chat-Bot-AI-Summary
This chat bot summarizes the data for both technical and non technical users.

# Censys Data Summarizer - AI Agent

A full-stack AI-powered application that analyzes and summarizes Censys host data using Perplexity AI. This project demonstrates prompt engineering, AI integration, and user interface design for cybersecurity data analysis.

## 🚀 Features

- **AI-Powered Analysis**: Uses Perplexity AI (Sonar model) for intelligent security data summarization
- **File Upload**: Upload JSON files containing Censys host data
- **Interactive UI**: Clean, responsive web interface with real-time analysis
- **Structured Output**: Generates comprehensive reports with executive summaries, metrics, and actionable insights
- **Markdown Rendering**: Professional formatting with tables, headings, and bullet points
- **Dual Audience**: Designed for both technical and non-technical users

## 📋 Project Structure

```
Proj_Deep/
├── app.py                 # Flask backend with Perplexity AI integration
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── script.js         # Frontend JavaScript with file upload
│   └── style.css         # Responsive CSS styling
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Perplexity AI API key

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd Proj_Deep
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key
Update the `PERPLEXITY_API_KEY` in `app.py` with your Perplexity API key:
```python
PERPLEXITY_API_KEY = "your-api-key-here"
```

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## 🎯 Usage

1. **Open the Application**: Navigate to `http://127.0.0.1:5000`
2. **Upload Data**: Click "Choose File" to upload a JSON file containing Censys host data
3. **Or Paste Data**: Alternatively, paste JSON data directly into the textarea
4. **Generate Summary**: Click "Generate Summary" to analyze the data
5. **View Results**: Review the structured security analysis report

### Sample Data Format
```json
{
  "hosts": [
    {
      "ip": "192.168.1.1",
      "location": {
        "country": "United States",
        "city": "New York"
      },
      "services": [
        {
          "port": 22,
          "protocol": "SSH",
          "software": [{"product": "openssh", "version": "8.2"}],
          "vulnerabilities": [
            {
              "cve_id": "CVE-2023-1234",
              "severity": "critical",
              "cvss_score": 9.8
            }
          ]
        }
      ],
      "threat_intelligence": {
        "risk_level": "high"
      }
    }
  ]
}
```

## 🧪 Testing

### Manual Testing
1. **File Upload Test**:
   - Upload a valid JSON file
   - Verify data loads correctly in textarea
   - Test with invalid file types (should show error)

2. **Data Analysis Test**:
   - Use sample Censys data
   - Verify all sections appear (Executive Summary, Metrics, etc.)
   - Check Markdown rendering (bold text, tables, headings)

3. **Error Handling Test**:
   - Submit empty data
   - Submit invalid JSON
   - Test with malformed data

### Automated Testing (Future Enhancement)
```bash
# Run tests (when implemented)
python -m pytest tests/
```

## 🤖 AI Techniques Implemented

### 1. Prompt Engineering
- **Structured Prompts**: Multi-section prompts with clear instructions
- **Context Awareness**: Prompts adapt to different data types and risk levels
- **Output Formatting**: Specific Markdown formatting requirements
- **Audience Targeting**: Dual-language approach for technical and non-technical users

### 2. LLM Integration
- **Perplexity AI API**: Uses Sonar model for analysis
- **Error Handling**: Robust API error management
- **Response Processing**: JSON parsing and content extraction

### 3. Data Processing
- **JSON Validation**: Client and server-side validation
- **Metrics Extraction**: Automated calculation of security metrics
- **Content Analysis**: Intelligent parsing of host data structures

## 📊 Output Format

The AI agent generates reports with:

1. **Executive Summary**: 2-3 sentences in plain language
2. **Quick Metrics**: Host counts, risk levels, vulnerability counts
3. **Overall Risk Assessment**: Concise risk analysis
4. **Key Vulnerabilities**: Detailed CVE table with severity scores
5. **Services and Security Issues**: Per-host analysis table
6. **Notable Observations**: Key findings and patterns
7. **Recommended Next Actions**: Prioritized remediation steps

## 🔧 Development Assumptions

- **Data Format**: Assumes standard Censys JSON structure with hosts array
- **API Limits**: Perplexity API rate limits and token usage
- **Browser Support**: Modern browsers with JavaScript enabled
- **Network**: Stable internet connection for API calls
- **Security**: API key stored in code (not recommended for production)

## 🚀 Future Enhancements

### Short Term (1-2 weeks)
- [ ] **Environment Variables**: Move API key to `.env` file
- [ ] **Input Validation**: Enhanced JSON schema validation
- [ ] **Error Recovery**: Better error messages and retry mechanisms
- [ ] **Loading States**: Progress indicators for long analyses
- [ ] **Export Features**: PDF/CSV export of reports

### Medium Term (1-2 months)
- [ ] **Authentication**: User login and session management
- [ ] **Database Integration**: Store analysis history and results
- [ ] **Batch Processing**: Analyze multiple datasets simultaneously
- [ ] **Custom Prompts**: User-defined analysis templates
- [ ] **API Rate Limiting**: Implement proper rate limiting and queuing

### Long Term (3-6 months)
- [ ] **Machine Learning**: Custom models for threat detection
- [ ] **Real-time Monitoring**: Live data feed integration
- [ ] **Collaboration**: Team sharing and commenting features
- [ ] **Advanced Analytics**: Trend analysis and reporting dashboards
- [ ] **Integration**: Connect with other security tools (SIEM, SOAR)

### Technical Improvements
- [ ] **Unit Tests**: Comprehensive test coverage
- [ ] **Docker**: Containerization for easy deployment
- [ ] **CI/CD**: Automated testing and deployment
- [ ] **Performance**: Caching and optimization
- [ ] **Security**: Input sanitization and API security

## 🏗️ Architecture

```
Frontend (HTML/CSS/JS)
    ↓ HTTP Requests
Flask Backend (Python)
    ↓ API Calls
Perplexity AI (LLM)
    ↓ Analysis
Structured Report (Markdown)
```

## 📝 API Documentation

### POST /summarize
Analyzes Censys host data and returns structured summary.

**Request Body:**
```json
{
  "hosts": [
    {
      "ip": "string",
      "location": {...},
      "services": [...],
      "threat_intelligence": {...}
    }
  ]
}
```

**Response:**
```json
{
  "metrics": {
    "total_hosts": 3,
    "critical_risk": 1,
    "high_risk": 2,
    "services_count": 11,
    "unique_vulnerabilities": 3,
    "countries": ["US", "CN"]
  },
  "summary": "Markdown formatted analysis...",
  "hosts_count": 3
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues:
- Create an issue in the repository
- Contact: [your-email@example.com]

---

**Note**: This project was developed as a take-home assignment for an AI Engineer intern position, demonstrating full-stack development skills and AI integration capabilities.
