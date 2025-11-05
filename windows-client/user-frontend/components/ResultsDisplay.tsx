'use client'

import { CheckCircle, XCircle, FileText, Award, Briefcase, MapPin, DollarSign, Clock } from 'lucide-react'

interface ResultsDisplayProps {
  results: any[]
}

export default function ResultsDisplay({ results }: ResultsDisplayProps) {
  return (
    <div className="mt-8 space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Processing Results</h2>
      
      {results.map((result, index) => (
        <div key={index} className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
          {/* Header */}
          <div className={`px-6 py-4 ${result.status === 'success' ? 'bg-green-50 border-b border-green-200' : 'bg-red-50 border-b border-red-200'}`}>
            <div className="flex items-center gap-3">
              {result.status === 'success' ? (
                <CheckCircle className="w-6 h-6 text-green-600" />
              ) : (
                <XCircle className="w-6 h-6 text-red-600" />
              )}
              <div className="flex-1">
                <h3 className="font-semibold text-gray-900">{result.filename}</h3>
                <p className={`text-sm ${result.status === 'success' ? 'text-green-700' : 'text-red-700'}`}>
                  {result.status === 'success' ? 'Successfully processed' : 'Processing failed'}
                </p>
              </div>
            </div>
          </div>

          {/* Content */}
          {result.status === 'success' && result.data && (
            <div className="p-6 space-y-6">
              {/* Document Type */}
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <FileText className="w-5 h-5 text-blue-600" />
                  <h4 className="font-semibold text-gray-900">Document Type</h4>
                </div>
                <p className="text-lg text-gray-700 bg-blue-50 px-4 py-2 rounded-lg inline-block">
                  {result.data.document_type}
                </p>
              </div>

              {/* Skills */}
              {result.data.skills && result.data.skills.length > 0 && (
                <div>
                  <div className="flex items-center gap-2 mb-3">
                    <Award className="w-5 h-5 text-purple-600" />
                    <h4 className="font-semibold text-gray-900">Extracted Skills</h4>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {result.data.skills.map((skill: string, idx: number) => (
                      <span
                        key={idx}
                        className="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm font-medium"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Metadata */}
              {result.data.metadata && Object.keys(result.data.metadata).length > 0 && (
                <div>
                  <h4 className="font-semibold text-gray-900 mb-3">Additional Information</h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {Object.entries(result.data.metadata).map(([key, value]: [string, any]) => (
                      value && value !== 'Not specified' && (
                        <div key={key} className="bg-gray-50 px-4 py-2 rounded-lg">
                          <p className="text-xs text-gray-600 uppercase tracking-wide mb-1">
                            {key.replace(/_/g, ' ')}
                          </p>
                          <p className="text-sm text-gray-900 font-medium">
                            {Array.isArray(value) ? value.join(', ') : value}
                          </p>
                        </div>
                      )
                    ))}
                  </div>
                </div>
              )}

              {/* OCR Preview */}
              {result.data.ocr_preview && (
                <div>
                  <h4 className="font-semibold text-gray-900 mb-2">Extracted Text Preview</h4>
                  <div className="bg-gray-50 p-4 rounded-lg border border-gray-200 max-h-32 overflow-y-auto">
                    <p className="text-sm text-gray-700 whitespace-pre-wrap font-mono">
                      {result.data.ocr_preview}
                    </p>
                  </div>
                </div>
              )}

              {/* Job Recommendations */}
              {result.data.job_recommendations && result.data.job_recommendations.length > 0 && (
                <div>
                  <div className="flex items-center gap-2 mb-4">
                    <Briefcase className="w-5 h-5 text-green-600" />
                    <h4 className="font-semibold text-gray-900">Recommended Jobs</h4>
                  </div>
                  <div className="space-y-4">
                    {result.data.job_recommendations.map((job: any, idx: number) => (
                      <div key={idx} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                        <div className="flex items-start justify-between mb-2">
                          <div>
                            <h5 className="font-semibold text-gray-900 text-lg">{job.title}</h5>
                            <p className="text-sm text-gray-600">{job.company}</p>
                          </div>
                          {job.match_score > 0 && (
                            <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-semibold">
                              {job.match_score}% Match
                            </span>
                          )}
                        </div>
                        
                        <div className="flex flex-wrap gap-4 text-sm text-gray-600 mb-3">
                          <div className="flex items-center gap-1">
                            <MapPin className="w-4 h-4" />
                            <span>{job.location}</span>
                          </div>
                          <div className="flex items-center gap-1">
                            <DollarSign className="w-4 h-4" />
                            <span>{job.salary}</span>
                          </div>
                          <div className="flex items-center gap-1">
                            <Clock className="w-4 h-4" />
                            <span>{job.posted_date}</span>
                          </div>
                        </div>

                        <p className="text-sm text-gray-700 mb-3">{job.description}</p>

                        <div className="flex flex-wrap gap-2">
                          {job.required_skills.slice(0, 5).map((skill: string, skillIdx: number) => (
                            <span
                              key={skillIdx}
                              className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs"
                            >
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Error Message */}
          {result.status === 'error' && (
            <div className="p-6">
              <p className="text-red-700 bg-red-50 px-4 py-3 rounded-lg">
                <strong>Error:</strong> {result.error}
              </p>
            </div>
          )}
        </div>
      ))}
    </div>
  )
}
