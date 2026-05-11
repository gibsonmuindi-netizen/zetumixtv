'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { Header } from '@/components/Header'
import { API_BASE_URL } from '@/config/api'

interface WatchEntry {
  id: number
  video: number
  watched_at: string
  minutes_watched: number
  is_completed: boolean
}

export default function WatchHistory() {
  const router = useRouter()
  const [history, setHistory] = useState<WatchEntry[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null

  useEffect(() => {
    if (!token) {
      router.push('/auth/login')
      return
    }
    fetchHistory()
  }, [token, router])

  const fetchHistory = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/watchhistory/`, {
        headers: {
          'Authorization': `Token ${token}`,
        },
      })
      const data = await response.json()
      setHistory(data)
    } catch (err) {
      setError('Failed to load watch history')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header />
        <main className="container mx-auto px-4 py-8">
          <div className="text-center">Loading...</div>
        </main>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Watch History</h1>

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-8">
            {error}
          </div>
        )}

        {history.length === 0 ? (
          <div className="bg-white rounded-lg shadow-md p-8 text-center">
            <p className="text-gray-600 text-lg">No watch history yet</p>
            <p className="text-gray-500">Start watching videos to build your history</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-4">
            {history.map(entry => (
              <div key={entry.id} className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
                <div className="flex justify-between items-center">
                  <div>
                    <p className="text-gray-600 text-sm">Video #{entry.video}</p>
                    <p className="text-gray-700">Watched {entry.minutes_watched} minutes</p>
                  </div>
                  <div className="text-right">
                    <p className="text-gray-600 text-sm">
                      {new Date(entry.watched_at).toLocaleDateString()}
                    </p>
                    {entry.is_completed && (
                      <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-3 py-1 rounded-full">
                        Completed
                      </span>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}
