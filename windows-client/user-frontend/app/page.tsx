'use client'

import { useState } from 'react'
import { Upload, FileText, Briefcase, Award, Loader2, CheckCircle, XCircle } from 'lucide-react'
import FileUpload from '@/components/FileUpload'
import ResultsDisplay from '@/components/ResultsDisplay'

export default function Home() {
  const [username, setUsername] = useState('')
  const [results, setResults] = useState<any[]>([])
  const [isProcessing, setIsProcessing] = useState(false)

  const handleUploadComplete = (uploadResults: any[]) => {
    setResults(uploadResults)
    setIsProcessing(false)
  }

  const handleUploadStart = () => {
    setIsProcessing(true)
    setResults([])
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-blue-600 rounded-lg">
              <FileText className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">AI Document Parser</h1>
              <p className="text-sm text-gray-600">Upload academic documents for instant analysis</p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Username Input */}
        <div className="mb-8">
          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <label htmlFor="username" className="block text-sm font-semibold text-gray-700 mb-2">
              Enter Your Username
            </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="e.g., john_doe"
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
              disabled={isProcessing}
            />
            <p className="mt-2 text-xs text-gray-500">
              Your username helps organize documents on the server
            </p>
          </div>
        </div>

        {/* File Upload Section */}
        <FileUpload
          username={username}
          onUploadStart={handleUploadStart}
          onUploadComplete={handleUploadComplete}
          disabled={!username || isProcessing}
        />

        {/* Processing Indicator */}
        {isProcessing && (
          <div className="mt-8 bg-blue-50 border border-blue-200 rounded-xl p-6">
            <div className="flex items-center gap-3">
              <Loader2 className="w-6 h-6 text-blue-600 animate-spin" />
              <div>
                <h3 className="font-semibold text-blue-900">Processing Documents...</h3>
                <p className="text-sm text-blue-700">
                  Extracting text, analyzing content, and finding job matches
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Results Display */}
        {results.length > 0 && !isProcessing && (
          <ResultsDisplay results={results} />
        )}

        {/* Features Section */}
        {results.length === 0 && !isProcessing && (
          <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200">
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                <Upload className="w-6 h-6 text-blue-600" />
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Easy Upload</h3>
              <p className="text-sm text-gray-600">
                Drag and drop multiple documents or click to browse. Supports PDF, JPG, and PNG formats.
              </p>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                <Award className="w-6 h-6 text-purple-600" />
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">AI Analysis</h3>
              <p className="text-sm text-gray-600">
                Advanced OCR and AI technology extracts skills and categorizes your academic documents.
              </p>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                <Briefcase className="w-6 h-6 text-green-600" />
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Job Matching</h3>
              <p className="text-sm text-gray-600">
                Get personalized job recommendations based on the skills extracted from your certificates.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="mt-20 bg-gray-50 border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <p className="text-center text-sm text-gray-600">
            AI Document Parser © 2024 - Powered by EasyOCR & Gemini AI
          </p>
        </div>
      </footer>
    </main>
  )
}
