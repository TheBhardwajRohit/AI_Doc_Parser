'use client'

import { useState, useEffect } from 'react'
import { Server, Activity, FileText, Users, TrendingUp, RefreshCw, Eye, Trash2 } from 'lucide-react'
import axios from 'axios'
import DocumentModal from '@/components/DocumentModal'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function ServerDashboard() {
  const [health, setHealth] = useState<any>(null)
  const [documents, setDocuments] = useState<any[]>([])
  const [stats, setStats] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [selectedDoc, setSelectedDoc] = useState<any>(null)
  const [showModal, setShowModal] = useState(false)

  useEffect(() => {
    fetchData()
    // Auto-refresh every 30 seconds
    const interval = setInterval(fetchData, 30000)
    return () => clearInterval(interval)
  }, [])

  const fetchData = async () => {
    try {
      const [healthRes, docsRes, statsRes] = await Promise.all([
        axios.get(`${API_URL}/health`),
        axios.get(`${API_URL}/documents`),
        axios.get(`${API_URL}/stats`)
      ])
      
      setHealth(healthRes.data)
      setDocuments(docsRes.data.documents)
      setStats(statsRes.data.stats)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching data:', error)
      setLoading(false)
    }
  }

  const handleViewDocument = async (docId: number) => {
    try {
      const response = await axios.get(`${API_URL}/documents/${docId}`)
      setSelectedDoc(response.data.document)
      setShowModal(true)
    } catch (error) {
      console.error('Error fetching document:', error)
      alert('Failed to load document details')
    }
  }

  const handleDeleteDocument = async (docId: number) => {
    if (!confirm('Are you sure you want to delete this document?')) return
    
    try {
      await axios.delete(`${API_URL}/documents/${docId}`)
      alert('Document deleted successfully')
      fetchData() // Refresh data
    } catch (error) {
      console.error('Error deleting document:', error)
      alert('Failed to delete document')
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <RefreshCw className="w-12 h-12 text-green-600 animate-spin mx-auto mb-4" />
          <p className="text-gray-600">Loading server data...</p>
        </div>
      </div>
    )
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-green-50 via-white to-blue-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-green-600 rounded-lg">
                <Server className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gray-900">Server Dashboard</h1>
                <p className="text-sm text-gray-600">Monitor document processing server</p>
              </div>
            </div>
            <button
              onClick={fetchData}
              className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
            >
              <RefreshCw className="w-4 h-4" />
              Refresh
            </button>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Server Health */}
        <div className="mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Server Health</h2>
          <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <Activity className="w-6 h-6 text-green-600" />
                <div>
                  <p className="text-sm text-gray-600">Status</p>
                  <p className={`text-lg font-semibold ${health?.status === 'healthy' ? 'text-green-600' : 'text-yellow-600'}`}>
                    {health?.status?.toUpperCase() || 'UNKNOWN'}
                  </p>
                </div>
              </div>
              <div className="text-right">
                <p className="text-xs text-gray-500">Last Updated</p>
                <p className="text-sm font-medium text-gray-700">
                  {health?.timestamp ? new Date(health.timestamp).toLocaleString() : 'N/A'}
                </p>
              </div>
            </div>

            {/* Services Status */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
              <div className="bg-gray-50 rounded-lg p-4">
                <p className="text-sm text-gray-600 mb-1">Database</p>
                <div className="flex items-center gap-2">
                  <div className={`w-3 h-3 rounded-full ${health?.services?.database === 'online' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                  <p className="font-semibold text-gray-900">{health?.services?.database || 'Unknown'}</p>
                </div>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <p className="text-sm text-gray-600 mb-1">OCR Service</p>
                <div className="flex items-center gap-2">
                  <div className={`w-3 h-3 rounded-full ${health?.services?.ocr === 'online' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                  <p className="font-semibold text-gray-900">{health?.services?.ocr || 'Unknown'}</p>
                </div>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <p className="text-sm text-gray-600 mb-1">AI Service</p>
                <div className="flex items-center gap-2">
                  <div className={`w-3 h-3 rounded-full ${health?.services?.ai === 'online' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                  <p className="font-semibold text-gray-900">{health?.services?.ai || 'Unknown'}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Statistics */}
        {stats && (
          <div className="mb-8">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Statistics</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
                <div className="flex items-center gap-3 mb-2">
                  <FileText className="w-6 h-6 text-blue-600" />
                  <p className="text-sm text-gray-600">Total Documents</p>
                </div>
                <p className="text-3xl font-bold text-gray-900">{stats.total_documents || 0}</p>
              </div>
              <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
                <div className="flex items-center gap-3 mb-2">
                  <Users className="w-6 h-6 text-purple-600" />
                  <p className="text-sm text-gray-600">Unique Users</p>
                </div>
                <p className="text-3xl font-bold text-gray-900">
                  {stats.by_user ? Object.keys(stats.by_user).length : 0}
                </p>
              </div>
              <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
                <div className="flex items-center gap-3 mb-2">
                  <TrendingUp className="w-6 h-6 text-green-600" />
                  <p className="text-sm text-gray-600">Last 24 Hours</p>
                </div>
                <p className="text-3xl font-bold text-gray-900">{stats.recent_24h || 0}</p>
              </div>
            </div>
          </div>
        )}

        {/* Documents List */}
        <div>
          <h2 className="text-xl font-bold text-gray-900 mb-4">
            Processed Documents ({documents.length})
          </h2>
          <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
            {documents.length === 0 ? (
              <div className="p-12 text-center">
                <FileText className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                <p className="text-gray-500">No documents processed yet</p>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-gray-50 border-b border-gray-200">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        ID
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        Username
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        Filename
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        Document Type
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        Timestamp
                      </th>
                      <th className="px-6 py-3 text-right text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        Actions
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-200">
                    {documents.map((doc) => (
                      <tr key={doc.id} className="hover:bg-gray-50 transition-colors">
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                          #{doc.id}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                          {doc.username}
                        </td>
                        <td className="px-6 py-4 text-sm text-gray-700">
                          <div className="max-w-xs truncate">{doc.original_filename}</div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm">
                          <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs font-medium">
                            {doc.document_type}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                          {new Date(doc.timestamp).toLocaleString()}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                          <button
                            onClick={() => handleViewDocument(doc.id)}
                            className="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-700 rounded-lg hover:bg-green-200 transition-colors mr-2"
                          >
                            <Eye className="w-4 h-4" />
                            View
                          </button>
                          <button
                            onClick={() => handleDeleteDocument(doc.id)}
                            className="inline-flex items-center gap-1 px-3 py-1 bg-red-100 text-red-700 rounded-lg hover:bg-red-200 transition-colors"
                          >
                            <Trash2 className="w-4 h-4" />
                            Delete
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Document Modal */}
      {showModal && selectedDoc && (
        <DocumentModal
          document={selectedDoc}
          onClose={() => {
            setShowModal(false)
            setSelectedDoc(null)
          }}
        />
      )}
    </main>
  )
}
