import { useState } from 'react'
import './App.css'

import Title from './components/Title';
import InputURL from './components/InputURL';
import CreatedURL from './components/CreatedURL';
import ErrorMessage from './components/ErrorMessage';

function App() {
  const [shortURL, setShortURL] = useState(null);
  const [error, setError] = useState(null);

  return (
    <>
      <Title />
      <InputURL setShortURL={setShortURL} setError={setError} />
      {shortURL && !error && <CreatedURL shortURL={shortURL} />}
      {error && <ErrorMessage />}
    </>
  )
}

export default App
