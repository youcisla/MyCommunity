import { useState } from 'react'
import axios from 'axios'

function App() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleCreate = async () => {
    setLoading(true)
    try {
      const res = await axios.post('http://localhost:8000/create')
      setResult(res.data)
    } catch (e) {
      setResult({ error: 'Failed to create account' })
    }
    setLoading(false)
  }

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>KickBot Factory</h1>
      <button onClick={handleCreate} disabled={loading}>
        {loading ? 'Creating...' : 'Create Kick Account'}
      </button>
      {result && (
        <pre style={{ marginTop: '1rem', background: '#eee', padding: '1rem' }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}

export default App
