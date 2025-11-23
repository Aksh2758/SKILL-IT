import React, { useState} from 'react';
import './auth.css';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    const handleLogin = async (e) => {
      e.preventDefault();
    
      const res = await fetch("http://localhost:5001/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });
    
      const data = await res.json();
    
      if (res.ok) {
        localStorage.setItem("token", data.token);
        alert("Login successful");
        window.location.href = "/";
      } else {
        alert(data.error);
      }
    };
  
    return (
      <div className="auth-container">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <div>
            <label>Email:</label>
            <input 
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required 
            />
          </div>
          <div>
            <label>Password:</label>
            <input 
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              required 
            />
          </div>
          <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
      </div>
    );
};

export default LoginPage;
