import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Github, Linkedin, FileText, Briefcase, Layout, Mic, ChevronRight, Star } from 'lucide-react';

// --- COMPONENTS ---

// 1. The Robot Avatar (Currently CSS, swap with Spline <Spline /> later)
import Spline from '@splinetool/react-spline';

const RobotAvatar = () => {
  return (
    <div className="w-[400px] h-[400px]">
       <Spline scene="https://prod.spline.design/9sePV9Z1uhzAN5Qn/scene.splinecode" />
    </div>
  );
}

// 2. The Tool Card (For the Orbiting Phase)
const OrbitItem = ({ icon: Icon, label, angle, delay, onClick }) => {
  // Calculate position based on angle
  const radius = 220; // Distance from robot
  const x = Math.cos((angle * Math.PI) / 180) * radius;
  const y = Math.sin((angle * Math.PI) / 180) * radius;

  return (
    <motion.button
      initial={{ opacity: 0, scale: 0 }}
      animate={{ opacity: 1, scale: 1, x, y }}
      transition={{ delay: delay, duration: 0.5, type: "spring" }}
      whileHover={{ scale: 1.1, zIndex: 50 }}
      onClick={onClick}
      className="absolute top-1/2 left-1/2 w-36 h-36 -ml-18 -mt-18 flex flex-col items-center justify-center gap-3 bg-slate-800/80 backdrop-blur-md border border-blue-500/30 rounded-2xl shadow-xl hover:border-cyan-400 group cursor-pointer"
    >
      <div className="p-3 bg-blue-900/30 rounded-full group-hover:bg-cyan-500/20 transition-colors">
        <Icon className="w-8 h-8 text-cyan-400" />
      </div>
      <span className="text-sm font-medium text-slate-200">{label}</span>
    </motion.button>
  );
};

// --- MAIN APP COMPONENT ---

export default function SkillItPrototype() {
  const [view, setView] = useState('landing'); // 'landing' | 'login' | 'dashboard'
  const [loading, setLoading] = useState(false);
  const [typedText, setTypedText] = useState("");
  
  // Dynamic Dialogue System
  const dialogue = {
    landing: "Hello! I am Skill-Bot. I'm here to analyze and build your career.",
    login: "To proceed, I need to access your project history. Please verify your identity.",
    loading: "Scanning GitHub repositories... Analyzing Code Styles... Extracting Skills...",
    dashboard: "Sync Complete! I've prepared these tools based on your profile."
  };

  // Typing effect for the robot
  useEffect(() => {
    let targetText = dialogue[loading ? 'loading' : view];
    let i = 0;
    setTypedText("");
    const interval = setInterval(() => {
      setTypedText(targetText.slice(0, i + 1));
      i++;
      if (i > targetText.length) clearInterval(interval);
    }, 30);
    return () => clearInterval(interval);
  }, [view, loading]);

  // Handle Login Simulation
  const handleLogin = () => {
    setLoading(true);
    // Simulate API fetch delay
    setTimeout(() => {
      setLoading(false);
      setView('dashboard');
    }, 2500);
  };

  return (
    <div className="h-screen w-full bg-[#0B1120] text-white overflow-hidden relative font-sans selection:bg-cyan-500/30">
      
      {/* Background Ambience */}
      <div className="absolute inset-0 z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[600px] h-[600px] bg-blue-900/20 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[600px] h-[600px] bg-indigo-900/20 blur-[120px] rounded-full" />
        {/* Stars */}
        {[...Array(20)].map((_, i) => (
          <div key={i} className="absolute bg-white rounded-full animate-pulse" 
            style={{
              top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%`,
              width: Math.random() * 2 + 'px', height: Math.random() * 2 + 'px',
              opacity: Math.random() * 0.5 + 0.3, animationDelay: `${Math.random() * 2}s`
            }} 
          />
        ))}
      </div>

      {/* --- CONTENT CONTAINER --- */}
      <div className="relative z-10 w-full h-full flex items-center justify-center">

        {/* 🤖 THE ROBOT (The Anchor) */}
        <motion.div
          layout // This magic prop makes it slide smoothly between positions
          className="absolute flex flex-col items-center justify-center z-20"
          initial={false}
          animate={{
            left: view === 'login' ? '20%' : '50%', // Move left on login
            x: '-50%', // Center alignment fix
            scale: view === 'dashboard' ? 0.8 : 1 // Shrink on dashboard
          }}
          transition={{ type: "spring", stiffness: 50, damping: 20 }}
        >
          <RobotAvatar mood={loading ? "thinking" : "neutral"} />
          
          {/* Dialogue Bubble */}
          <motion.div 
            className="mt-6 bg-slate-900/80 backdrop-blur-md border border-slate-700 px-6 py-4 rounded-xl max-w-xs text-center shadow-2xl relative"
            layout
          >
            {/* Little triangle for speech bubble */}
            <div className="absolute -top-2 left-1/2 -ml-2 w-4 h-4 bg-slate-900 border-t border-l border-slate-700 transform rotate-45" />
            <p className="text-cyan-300 font-mono text-sm leading-relaxed min-h-[3rem]">
              {typedText}<span className="animate-pulse">_</span>
            </p>
          </motion.div>
        </motion.div>

        {/* --- SCENE 1: LANDING BUTTON --- */}
        <AnimatePresence>
          {view === 'landing' && (
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.9 }}
              className="absolute top-[65%] flex flex-col items-center gap-4"
            >
              <button 
                onClick={() => setView('login')}
                className="group relative px-8 py-4 bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-bold text-lg rounded-full shadow-[0_0_20px_rgba(34,211,238,0.5)] transition-all flex items-center gap-2 overflow-hidden"
              >
                <div className="absolute inset-0 w-full h-full bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-500 skew-x-12" />
                <span className="relative z-10">Initialize System</span>
                <ChevronRight className="w-5 h-5 relative z-10 group-hover:translate-x-1 transition-transform" />
              </button>
              <p className="text-slate-500 text-sm uppercase tracking-widest">v2.0.1 Stable</p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* --- SCENE 2: LOGIN FORM --- */}
        <AnimatePresence>
          {view === 'login' && !loading && (
            <motion.div
              initial={{ x: 100, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: 100, opacity: 0 }}
              transition={{ delay: 0.3 }}
              className="absolute right-[10%] w-[400px] p-8 bg-slate-800/50 backdrop-blur-xl border border-slate-700 rounded-3xl shadow-2xl"
            >
              <h2 className="text-2xl font-bold text-white mb-2">Identify User</h2>
              <p className="text-slate-400 text-sm mb-6">Connect reliable data sources.</p>

              <div className="space-y-3">
                <button 
                  onClick={handleLogin}
                  className="w-full flex items-center justify-center gap-3 py-3 bg-[#24292e] hover:bg-[#2f363d] rounded-xl border border-slate-600 transition-all group"
                >
                  <Github className="w-5 h-5 text-white" />
                  <span>Import from GitHub</span>
                </button>
                
                <button 
                  onClick={handleLogin}
                  className="w-full flex items-center justify-center gap-3 py-3 bg-[#0077b5] hover:bg-[#006097] rounded-xl transition-all"
                >
                  <Linkedin className="w-5 h-5 text-white" />
                  <span>Import from LinkedIn</span>
                </button>
              </div>

              <div className="mt-6 pt-6 border-t border-slate-700/50 text-center">
                <button className="text-slate-500 text-sm hover:text-cyan-400 transition-colors">
                  Skip & Enter Data Manually
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* --- SCENE 2.5: LOADING STATE (Scanning) --- */}
        {loading && (
            <div className="absolute top-[65%] w-64 h-1 bg-slate-800 rounded-full overflow-hidden">
                <motion.div 
                    className="h-full bg-cyan-500 shadow-[0_0_10px_#22d3ee]"
                    initial={{ width: "0%" }}
                    animate={{ width: "100%" }}
                    transition={{ duration: 2.5 }}
                />
            </div>
        )}

        {/* --- SCENE 3: ORBITING DASHBOARD --- */}
        <AnimatePresence>
          {view === 'dashboard' && (
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
              <div className="relative w-[500px] h-[500px] flex items-center justify-center pointer-events-auto">
                {/* Orbit Rings (Visual only) */}
                <div className="absolute inset-0 border border-slate-700/30 rounded-full animate-[spin_10s_linear_infinite]" />
                <div className="absolute inset-10 border border-slate-700/20 rounded-full animate-[spin_15s_linear_infinite_reverse]" />
                
                {/* The Floating Tools */}
                <OrbitItem icon={FileText} label="Resume Builder" angle={-90} delay={0.2} onClick={() => alert("Open Resume")} />
                <OrbitItem icon={Briefcase} label="Job Match" angle={0} delay={0.4} onClick={() => alert("Open Jobs")} />
                <OrbitItem icon={Layout} label="Portfolio" angle={90} delay={0.6} onClick={() => alert("Open Portfolio")} />
                <OrbitItem icon={Mic} label="Interview AI" angle={180} delay={0.8} onClick={() => alert("Open Interview")} />
              </div>
            </div>
          )}
        </AnimatePresence>

      </div>
    </div>
  );
}