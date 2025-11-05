'use client'

import { X, FileText, Award, Briefcase } from 'lucide-react'

interface DocumentModalProps {
  document: any
  onClose: () => void
}

export default function DocumentModal({ document, onClose }: DocumentModalProps) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-green-600 to-blue-600 px-6 py-4 flex items-center justify-between">
          <h2 className="text-xl font-bold text-white">Document Details</h2>
          <button
            onClick={onClose}
            className="p-1 hover:bg-white/20 rounded-full transition-colors"
          >
            <X className="w-6 h-6 text-white" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto max-h-[calc(90vh-80px)]">
          {/* Basic Info */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-3">Basic Information</h3>
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-xs text-gray-600 mb-1">Document ID</p>
                <p className="font-semibold text-gray-900">#{document.id}</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-xs text-gray-600 mb-1">Username</p>
                <p className="font-semibold text-gray-900">{document.username}</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg col-span-2">
                <p className="text-xs text-gray-600 mb-1">Filename</p>
                <p className="font-semibold text-gray-900">{document.original_filename}</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-xs text-gray-600 mb-1">Document Type</p>
                <p className="font-semibold text-blue-700">{document.document_type}</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-xs text-gray-600 mb-1">Processed At</p>
                <p className="font-semibold text-gray-900">
                  {new Date(document.timestamp).toLocaleString()}
                </p>
              </div>
            </div>
          </div>

          {/* Skills */}
          {document.skills && document.skills.length > 0 && (
            <div className="mb-6">
              <div className="flex items-center gap-2 mb-3">
                <Award className="w-5 h-5 text-purple-600" />
                <h3 className="text-lg font-semibold text-gray-900">Extracted Skills</h3>
              </div>
              <div className="flex flex-wrap gap-2">
                {document.skills.map((skill: string, idx: number) => (
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
          {document.metadata && Object.keys(document.metadata).length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-3">Metadata</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {Object.entries(document.metadata).map(([key, value]: [string, any]) => (
                  value && value !== 'Not specified' && (
                    <div key={key} className="bg-gray-50 p-3 rounded-lg">
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

          {/* Job Recommendations */}
          {document.job_recommendations && document.job_recommendations.length > 0 && (
            <div className="mb-6">
              <div className="flex items-center gap-2 mb-3">
                <Briefcase className="w-5 h-5 text-green-600" />
                <h3 className="text-lg font-semibold text-gray-900">Job Recommendations</h3>
              </div>
              <div className="space-y-3">
                {document.job_recommendations.map((job: any, idx: number) => (
                  <div key={idx} className="border border-gray-200 rounded-lg p-4">
                    <div className="flex items-start justify-between mb-2">
                      <div>
                        <h4 className="font-semibold text-gray-900">{job.title}</h4>
                        <p className="text-sm text-gray-600">{job.company}</p>
                      </div>
                      {job.match_score > 0 && (
                        <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs font-semibold">
                          {job.match_score}% Match
                        </span>
                      )}
                    </div>
                    <p className="text-sm text-gray-700 mb-2">{job.description}</p>
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

          {/* OCR Text */}
          {document.ocr_text && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <FileText className="w-5 h-5 text-blue-600" />
                <h3 className="text-lg font-semibold text-gray-900">Extracted Text</h3>
              </div>
              <div className="bg-gray-50 p-4 rounded-lg border border-gray-200 max-h-64 overflow-y-auto">
                <pre className="text-sm text-gray-700 whitespace-pre-wrap font-mono">
                  {document.ocr_text}
                </pre>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
