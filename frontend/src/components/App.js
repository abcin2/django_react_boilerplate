import React from 'react';
import { render } from "react-dom";

function App() {
    return (
        <div>
            <h1>hello world!</h1>
        </div>
    )
}

export default App

const appDiv = document.getElementById('app');
render(<App />, appDiv)
