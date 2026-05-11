'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { Header } from '@/components/Header'
import { API_BASE_URL } from '@/config/api'

interface SubscriptionPlan {
  id: number
  plan_name: string
  price: string
  duration_days: number
  description: string
  includes_hd: boolean
  max_streams: number
  includes_offline: boolean
}

export default function Subscriptions() {
  const router = useRouter()
  const [plans, setPlans] = useState<SubscriptionPlan[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null

  useEffect(() => {
    if (!token) {
      router.push('/auth/login')
      return
    }
    fetchPlans()
  }, [token, router])

  const fetchPlans = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/subscriptions/plans/`, {
        headers: {
          'Authorization': `Token ${token}`,
        },
      })
      const data = await response.json()
      setPlans(data)
    } catch (err) {
      setError('Failed to load subscription plans')
    } finally {
      setLoading(false)
    }
  }

  const handleSubscribe = async (planId: number) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/subscriptions/subscribe/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({ plan_id: planId }),
      })
      if (response.ok) {
        alert('Subscription successful!')
        router.push('/dashboard')
      } else {
        alert('Subscription failed')
      }
    } catch (err) {
      alert('Error subscribing to plan')
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
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Choose Your Plan</h1>

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-8">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {plans.map(plan => (
            <div key={plan.id} className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
              <h3 className="text-2xl font-bold text-gray-900 mb-2">{plan.plan_name}</h3>
              <div className="text-3xl font-bold text-blue-600 mb-4">KSH {plan.price}</div>
              <p className="text-gray-600 text-sm mb-4">{plan.duration_days} days</p>

              {plan.description && (
                <p className="text-gray-700 text-sm mb-4">{plan.description}</p>
              )}

              <ul className="space-y-2 mb-6 text-sm">
                {plan.includes_hd && <li className="text-green-600">✓ HD Quality</li>}
                <li className="text-gray-600">Max {plan.max_streams} stream(s)</li>
                {plan.includes_offline && <li className="text-green-600">✓ Offline Download</li>}
              </ul>

              <button
                onClick={() => handleSubscribe(plan.id)}
                className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors"
              >
                Subscribe
              </button>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}
