import { useState } from 'react';
import { FaArrowRight } from 'react-icons/fa';
import styled from 'styled-components';

import { shortenURL as apiShortenURL } from '../api';

const InputTaskWrapper = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: baseline;
  column-gap: 20px;
  width: 100%;
`;

const InputLabel = styled.label`
  font-size: 1.2em;
`;

const StyledInput = styled.input`
  font-size: 1.2em;
`;

const InputURL = ({ setShortURL, setError = () => {} }) => {
  const [longURL, setLongURL] = useState('');

  const shortenURL = async () => {
    if (longURL === '') {
      return;
    }

    setError(null);

    try {
      const shortURL = await apiShortenURL(longURL);
      setShortURL(shortURL);
      setLongURL('');
    } catch (e) {
      setError(e);
    }
  };

  return (
    <InputTaskWrapper>
      <InputLabel>
        URL to Shorten:
      </InputLabel>
      <StyledInput
        type='text'
        value={longURL}
        onChange={(e) => { setLongURL(e.target.value) }}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            shortenURL()
          }
        }}
      />
      <button onClick={() => shortenURL()}>
        <FaArrowRight />
      </button>
    </InputTaskWrapper>
  );
};

export default InputURL;