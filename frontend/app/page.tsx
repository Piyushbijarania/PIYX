export default function Home() {
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
                />
                <div className="flex items-center justify-between px-3 py-1.5">
                  <div className="flex items-center gap-2">
                    <button className="flex items-center gap-2 bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors">
                      <span className="text-xs">➕</span>
                      <span>Upload</span>
                    </button>
                    <button className="flex items-center gap-2 bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors">
                      <span className="text-xs">⏱️</span>
                      <span>1 min</span>
                    </button>
                    <button className="flex items-center gap-2 bg-gray-800/80 hover:bg-gray-700 px-3 py-1.5 rounded-full text-sm transition-colors">
                      <span className="text-xs">🌐</span>
                      <span>English</span>
                    </button>
                  </div>
                  <button className="bg-gray-700/80 hover:bg-gray-600 p-2 rounded-full transition-colors">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            {/* CTA Button */}
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mt-6 mb-6">
              <button className="bg-gradient-to-r from-gray-800 to-gray-900 hover:from-gray-700 hover:to-gray-800 text-white px-8 py-4 rounded-full text-lg font-semibold transition-all hover:scale-105 shadow-lg shadow-gray-900/50 border border-white/10">
                Watch AI-Generated Video Explanations
              </button>
            </div>

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
            {/* Step 1 */}
            <div className="bg-gray-800/50 backdrop-blur-sm border border-white/10 rounded-2xl p-8 hover:border-blue-500/50 transition-all">
              <div className="text-5xl mb-4">📤</div>
              <h3 className="text-2xl font-bold mb-3">Ask Anything</h3>
              <p className="text-gray-400">
                Type your question or upload an image of your doubt from textbook, whiteboard, or phone.
              </p>
            </div>

            {/* Step 2 */}
            <div className="bg-gray-800/50 backdrop-blur-sm border border-white/10 rounded-2xl p-8 hover:border-blue-500/50 transition-all">
              <div className="text-5xl mb-4">⚡</div>
              <h3 className="text-2xl font-bold mb-3">AI Generates Your Video</h3>
              <p className="text-gray-400">
                Our advanced AI engine analyzes your question and creates a unique animated video explanation.
              </p>
            </div>

            {/* Step 3 */}
            <div className="bg-gray-800/50 backdrop-blur-sm border border-white/10 rounded-2xl p-8 hover:border-blue-500/50 transition-all">
              <div className="text-5xl mb-4">🎓</div>
              <h3 className="text-2xl font-bold mb-3">Watch, Learn & Master</h3>
              <p className="text-gray-400">
                Get animated, crystal-clear video answers that boost recall and understanding.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            Stop Reading. Start Watching.
          </h2>
          <p className="text-xl text-gray-400 mb-8">
            You&apos;re one click away from the future of learning. Get the power of a personal AI study helper.
          </p>
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-full text-lg font-semibold transition-all hover:scale-105 shadow-lg shadow-blue-600/50">
            Get Started
          </button>
          <p className="text-gray-500 text-sm mt-4">
            No credit card required • Unlimited videos • Always free
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 py-12 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <h4 className="font-bold text-lg mb-4">PIYX AI</h4>
              <p className="text-gray-400 text-sm">
                The future of learning with AI-powered video explanations.
              </p>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Platform</h4>
              <ul className="space-y-2 text-gray-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition-colors">Features</a></li>
                <li><a href="#" className="hover:text-blue-400 transition-colors">How it Works</a></li>
                <li><a href="#" className="hover:text-blue-400 transition-colors">Pricing</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Resources</h4>
              <ul className="space-y-2 text-gray-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition-colors">Documentation</a></li>
                <li><a href="#" className="hover:text-blue-400 transition-colors">Support</a></li>
                <li><a href="#" className="hover:text-blue-400 transition-colors">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Get In Touch</h4>
              <p className="text-gray-400 text-sm">support@piyx.ai</p>
            </div>
          </div>
          <div className="border-t border-white/10 pt-8 text-center text-gray-500 text-sm">
            <p>Copyright © 2025 PIYX AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
