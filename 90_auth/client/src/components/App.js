import Home from './Home'
import Main from './Main'
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <div className="App">

        <Routes>
          <Route 
                path="/" 
                element={<Home />} />

          <Route 
              path="/main" 
              element={<Main />} />

        </Routes>

    </div>
  );
}

export default App;