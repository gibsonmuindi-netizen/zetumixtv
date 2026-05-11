'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { Header } from '@/components/Header'

interface User {
  id: number
  email: string
  username: string
  subscription_status: string
  phone_number: string
}

export default function Dashboard() {
  const router = useRouter()
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const userStr = localStorage.getItem('user')
    const token = localStorage.getItem('token')

    if (!userStr || !token) {
      router.push('/auth/login')
      return
    }

    setUser(JSON.parse(userStr))
    setLoading(false)
  }, [router])

  const handleLogout = () => {
    localStorage.removeItem('user')
    localStorage.removeItem('token')
    router.push('/')
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
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="md:col-span-1">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Account</h2>
              <div className="space-y-3">
                <div>
                  <p className="text-sm text-gray-600">Email</p>
                  <p className="text-lg text-gray-900">{user?.email}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600">Username</p>
                  <p className="text-lg text-gray-900">{user?.username}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600">Subscription</p>
                  <p className="text-lg font-semibold text-blue-600">
                    {user?.subscription_status || 'Free'}
                  </p>
                </div>
                {user?.phone_number && (
                  <div>
                    <p className="text-sm text-gray-600">Phone</p>
                    <p className="text-lg text-gray-900">{user.phone_number}</p>
                  </div>
                )}
              </div>
              <button
                onClick={handleLogout}
                className="w-full mt-6 bg-red-600 text-white py-2 rounded-lg hover:bg-red-700 transition-colors"
              >
                Logout
              </button>
            </div>
          </div>

          <div className="md:col-span-2">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Link href="/subscriptions" className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer">
                <div className="text-3xl mb-2">💳</div>
                <h3 className="text-lg font-bold text-gray-900">Subscriptions</h3>
                <p className="text-gray-600 mt-2">View and manage your subscription plans</p>
              </Link>

              <Link href="/watch-history" className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer">
                <div className="text-3xl mb-2">📺</div>
                <h3 className="text-lg font-bold text-gray-900">Watch History</h3>
                <p className="text-gray-600 mt-2">View your watch history and recommendations</p>
              </Link>

              <Link href="/payments" className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer">
                <div className="text-3xl mb-2">💰</div>
                <h3 className="text-lg font-bold text-gray-900">Payments</h3>
                <p className="text-gray-600 mt-2">View your payment history and transactions</p>
              </Link>

              <Link href="/" className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer">
                <div className="text-3xl mb-2">🎬</div>
                <h3 className="text-lg font-bold text-gray-900">Browse Content</h3>
                <p className="text-gray-600 mt-2">Explore all available videos and categories</p>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
