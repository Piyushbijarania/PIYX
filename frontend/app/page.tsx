"use client";

import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [duration, setDuration] = useState(60);
  const [isGenerating, setIsGenerating] = useState(false);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async () => {
    if (!question.trim()) {
      setError("Please enter a question");
      return;
    }

    setIsGenerating(true);
    setError(null);
    setVideoUrl(null);

    try {
      const response = await fetch("http://localhost:8000/generate-video", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
          duration: duration,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to generate video");
      }

      const data = await response.json();
      
      if (data.success && data.video_url) {
        setVideoUrl(`http://localhost:8000${data.video_url}`);
      } else {
        throw new Error("Video generation failed");
      }
    } catch (err: any) {
      setError(err.message || "An error occurred while generating the video");
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white">
      {/* Navigation */}
      <nav className="fixed top-0 w-full bg-[#0a0a0a]/80 backdrop-blur-md border-b border-white/10 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="text-2xl font-bold">PIYX AI</div>
          <div className="flex items-center gap-6">
            <a href="#features" className="hover:text-blue-400 transition-colors">Features</a>
            <a href="#how-it-works" className="hover:text-blue-400 transition-colors">How it Works</a>
            <button className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-full transition-colors">
              Get Started
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6 min-h-screen flex items-center">
        <div className="max-w-7xl mx-auto w-full">
          <div className="text-center max-w-5xl mx-auto">
            {/* Main Heading */}
            <h1 className="text-6xl md:text-7xl lg:text-8xl font-bold mb-6 leading-tight">
              <span className="bg-gradient-to-r from-white via-blue-100 to-blue-300 bg-clip-text text-transparent">
                Live Audio-Video
              </span>
              <br />
              <span className="text-white">Explanation</span>
            </h1>

            {/* Subheading */}
            <p className="text-xl md:text-2xl text-gray-400 mb-10 max-w-2xl mx-auto relative">
              <span className="inline-block animate-[fadeIn_1s_ease-in-out] relative">
                Where <span className="text-white font-semibold relative inline-block">
                  <span className="relative z-10">prompts</span>
                  <span className="absolute top-0 left-0 w-[400%] h-full -translate-x-full animate-[glareTravel_3s_ease-in-out_infinite] pointer-events-none">
                    <span className="absolute inset-0 bg-gradient-to-r from-transparent via-white/25 to-transparent blur-sm"></span>
                  </span>
                </span> become <span className="text-white font-semibold">professors</span>
              </span>
            </p>

            {/* Interactive Input Section */}
            <div className="mb-6 max-w-4xl mx-auto">
              <div className="bg-gradient-to-br from-gray-900/50 to-gray-800/50 border border-white/10 rounded-2xl p-1.5 shadow-2xl backdrop-blur-sm">
                <textarea
                  placeholder="Ask a question (will generate video)..."
                  className="w-full bg-transparent text-white placeholder-gray-500 px-6 py-3 rounded-xl focus:outline-none resize-none text-base"
                  rows={2}
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  disabled={isGenerating}
                />
                <div className="flex items-center justify-between px-3 py-1.5">
                  <div className="flex items-center gap-2">
                    <button 
                      className="flex items-center gap-2 bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors"
                      disabled={isGenerating}
                    >
                      <span className="text-xs">➕</span>
                      <span>Upload</span>
                    </button>
                    <select
                      className="bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors cursor-pointer"
                      value={duration}
                      onChange={(e) => setDuration(Number(e.target.value))}
                      disabled={isGenerating}
                    >
                      <option value={30}>30 sec</option>
                      <option value={60}>1 min</option>
                      <option value={90}>1.5 min</option>
                      <option value={120}>2 min</option>
                    </select>
                    <button 
                      className="flex items-center gap-2 bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors"
                      disabled={isGenerating}
                    >
                      <span className="text-xs">🌐</span>
                      <span>English</span>
                    </button>
                  </div>
                  <button 
                    className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed p-2 rounded-full transition-colors"
                    onClick={handleGenerate}
                    disabled={isGenerating || !question.trim()}
                  >
                    {isGenerating ? (
                      <svg className="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                    ) : (
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
                      </svg>
                    )}
                  </button>
                </div>
              </div>
            </div>

            {/* Error Display */}
            {error && (
              <div className="mb-6 max-w-4xl mx-auto bg-red-900/20 border border-red-500/30 rounded-xl p-4">
                <p className="text-red-400">{error}</p>
              </div>
            )}

            {/* Loading State */}
            {isGenerating && (
              <div className="mb-6 max-w-4xl mx-auto bg-blue-900/20 border border-blue-500/30 rounded-xl p-6">
                <div className="flex items-center justify-center gap-3">
                  <svg className="w-6 h-6 animate-spin" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <p className="text-blue-300">Generating your educational video...</p>
                </div>
                <p className="text-gray-400 text-sm mt-2">This may take 30-60 seconds</p>
              </div>
            )}

            {/* Video Display */}
            {videoUrl && !isGenerating && (
              <div className="mb-6 max-w-4xl mx-auto bg-gradient-to-br from-gray-900/50 to-gray-800/50 border border-white/10 rounded-2xl p-4 shadow-2xl">
                <video 
                  controls 
                  className="w-full rounded-xl"
                  autoPlay
                >
                  <source src={videoUrl} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
                <div className="mt-4 flex gap-2">
                  <button 
                    className="flex-1 bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg transition-colors"
                    onClick={() => window.open(videoUrl, '_blank')}
                  >
                    Download Video
                  </button>
                  <button 
                    className="flex-1 bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded-lg transition-colors"
                    onClick={() => {
                      setVideoUrl(null);
                      setQuestion("");
                    }}
                  >
                    Generate New Video
                  </button>
                </div>
              </div>
            )}

            {/* CTA Button */}
            {!videoUrl && !isGenerating && (
              <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mt-6 mb-6">
                <button className="bg-gradient-to-r from-gray-800 to-gray-900 hover:from-gray-700 hover:to-gray-800 text-white px-8 py-4 rounded-full text-lg font-semibold transition-all hover:scale-105 shadow-lg shadow-gray-900/50 border border-white/10">
                  Watch AI-Generated Video Explanations
                </button>
              </div>
            )}

            {/* Trust Badge */}
            <p className="text-gray-500 text-sm mb-20">
              Join 10,000+ students preparing with AI-powered video explanations
            </p>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-6 bg-gradient-to-b from-[#0a0a0a] to-gray-900">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-4">
              Your Personal Video Tutor in 3 Steps
            </h2>
            <p className="text-gray-400 text-lg">
              From question to crystal-clear video explanation in just 30 seconds
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-gray-900/50 border border-white/10 rounded-2xl p-8">
              <div className="text-4xl mb-4">📝</div>
              <h3 className="text-2xl font-bold mb-3">1. Ask Your Question</h3>
              <p className="text-gray-400">
                Type any concept you want to understand - math, science, coding, or any topic
              </p>
            </div>

            <div className="bg-gray-900/50 border border-white/10 rounded-2xl p-8">
              <div className="text-4xl mb-4">🤖</div>
              <h3 className="text-2xl font-bold mb-3">2. AI Creates Video</h3>
              <p className="text-gray-400">
                Our AI generates custom animations and explanations tailored to your question
              </p>
            </div>

            <div className="bg-gray-900/50 border border-white/10 rounded-2xl p-8">
              <div className="text-4xl mb-4">🎬</div>
              <h3 className="text-2xl font-bold mb-3">3. Watch & Learn</h3>
              <p className="text-gray-400">
                Get a personalized video explanation with visual animations in seconds
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
