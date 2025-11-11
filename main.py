import React, { useState } from 'react';
import { Users, TrendingUp, Cloud, Star, Target, Award, Activity, Zap } from 'lucide-react';

const FantasyCricketAI = () => {
  const [players, setPlayers] = useState([]);
  const [matchDetails, setMatchDetails] = useState({
    team1: '',
    team2: '',
    venue: '',
    weather: 'sunny',
    pitchType: 'balanced',
    tossWinner: '',
    tossDecision: ''
  });
  const [playerInput, setPlayerInput] = useState('');
  const [budget, setBudget] = useState(100);
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(false);

  // Sample player database with comprehensive stats
  const samplePlayers = [
    // Batsmen
    { name: "Virat Kohli", team: "IND", role: "Batsman", recentForm: 92, price: 11.5, mulank: 8, bhagyank: 5 },
    { name: "Rohit Sharma", team: "IND", role: "Batsman", recentForm: 88, price: 11.0, mulank: 3, bhagyank: 7 },
    { name: "Steve Smith", team: "AUS", role: "Batsman", recentForm: 85, price: 10.5, mulank: 1, bhagyank: 9 },
    { name: "Babar Azam", team: "PAK", role: "Batsman", recentForm: 90, price: 11.0, mulank: 5, bhagyank: 3 },
    { name: "Kane Williamson", team: "NZ", role: "Batsman", recentForm: 87, price: 10.5, mulank: 2, bhagyank: 6 },
    { name: "Joe Root", team: "ENG", role: "Batsman", recentForm: 89, price: 10.5, mulank: 9, bhagyank: 4 },
    
    // All-rounders
    { name: "Hardik Pandya", team: "IND", role: "All-Rounder", recentForm: 86, price: 10.0, mulank: 7, bhagyank: 8 },
    { name: "Ben Stokes", team: "ENG", role: "All-Rounder", recentForm: 84, price: 10.0, mulank: 6, bhagyank: 2 },
    { name: "Glenn Maxwell", team: "AUS", role: "All-Rounder", recentForm: 82, price: 9.5, mulank: 4, bhagyank: 1 },
    { name: "Shakib Al Hasan", team: "BAN", role: "All-Rounder", recentForm: 83, price: 9.5, mulank: 3, bhagyank: 7 },
    { name: "Ravindra Jadeja", team: "IND", role: "All-Rounder", recentForm: 85, price: 9.5, mulank: 8, bhagyank: 5 },
    
    // Bowlers
    { name: "Jasprit Bumrah", team: "IND", role: "Bowler", recentForm: 94, price: 10.5, mulank: 2, bhagyank: 9 },
    { name: "Pat Cummins", team: "AUS", role: "Bowler", recentForm: 91, price: 10.0, mulank: 5, bhagyank: 3 },
    { name: "Shaheen Afridi", team: "PAK", role: "Bowler", recentForm: 90, price: 10.0, mulank: 1, bhagyank: 6 },
    { name: "Rashid Khan", team: "AFG", role: "Bowler", recentForm: 93, price: 10.5, mulank: 9, bhagyank: 4 },
    { name: "Trent Boult", team: "NZ", role: "Bowler", recentForm: 88, price: 9.5, mulank: 7, bhagyank: 8 },
    { name: "Kagiso Rabada", team: "SA", role: "Bowler", recentForm: 89, price: 10.0, mulank: 4, bhagyank: 2 },
    
    // Wicket-keepers
    { name: "Rishabh Pant", team: "IND", role: "WK-Batsman", recentForm: 86, price: 10.0, mulank: 6, bhagyank: 1 },
    { name: "Jos Buttler", team: "ENG", role: "WK-Batsman", recentForm: 88, price: 10.5, mulank: 3, bhagyank: 7 },
    { name: "Quinton de Kock", team: "SA", role: "WK-Batsman", recentForm: 84, price: 9.5, mulank: 8, bhagyank: 5 },
    { name: "Mohammad Rizwan", team: "PAK", role: "WK-Batsman", recentForm: 87, price: 9.5, mulank: 2, bhagyank: 9 },
    { name: "Alex Carey", team: "AUS", role: "WK-Batsman", recentForm: 81, price: 9.0, mulank: 5, bhagyank: 3 },
    { name: "KL Rahul", team: "IND", role: "WK-Batsman", recentForm: 85, price: 10.0, mulank: 1, bhagyank: 6 }
  ];

  const loadSamplePlayers = () => {
    setPlayers(samplePlayers);
  };

  const addPlayer = () => {
    if (playerInput.trim() && players.length < 22) {
      const newPlayer = {
        name: playerInput,
        team: matchDetails.team1 || "TEAM",
        role: "All-Rounder",
        recentForm: Math.floor(Math.random() * 30) + 70,
        price: Math.floor(Math.random() * 50) / 10 + 8,
        mulank: Math.floor(Math.random() * 9) + 1,
        bhagyank: Math.floor(Math.random() * 9) + 1
      };
      setPlayers([...players, newPlayer]);
      setPlayerInput('');
    }
  };

  const calculateAstrologyScore = (player, date = new Date()) => {
    const dayNumber = date.getDate();
    const luckyNumbers = [player.mulank, player.bhagyank];
    const dayCompatibility = luckyNumbers.includes(dayNumber % 9 || 9) ? 15 : 0;
    const numerologyBonus = (player.mulank + player.bhagyank) % 9 === dayNumber % 9 ? 10 : 5;
    return dayCompatibility + numerologyBonus;
  };

  const calculateVenueScore = (player, pitchType, weather) => {
    let score = 0;
    
    // Pitch compatibility
    if (pitchType === 'batting' && ['Batsman', 'WK-Batsman'].includes(player.role)) score += 15;
    if (pitchType === 'bowling' && player.role === 'Bowler') score += 15;
    if (pitchType === 'balanced' && player.role === 'All-Rounder') score += 10;
    
    // Weather impact
    if (weather === 'cloudy' && player.role === 'Bowler') score += 10;
    if (weather === 'sunny' && ['Batsman', 'WK-Batsman'].includes(player.role)) score += 10;
    if (weather === 'humid' && player.role === 'Bowler') score += 8;
    
    return score;
  };

  const calculateMLPrediction = (player, matchDetails) => {
    // Simulated ML prediction considering multiple factors
    const formWeight = player.recentForm * 0.3;
    const astrologyWeight = calculateAstrologyScore(player) * 0.15;
    const venueWeight = calculateVenueScore(player, matchDetails.pitchType, matchDetails.weather) * 0.25;
    const priceEfficiency = (player.recentForm / player.price) * 0.2;
    const randomFactor = Math.random() * 10 * 0.1; // Unpredictability factor
    
    return formWeight + astrologyWeight + venueWeight + priceEfficiency + randomFactor;
  };

  const analyzeHeadToHead = (player, opposingTeam) => {
    // Simulated H2H analysis
    const performanceMap = {
      'IND': [0.85, 0.92, 0.78, 0.88, 0.91],
      'AUS': [0.82, 0.87, 0.90, 0.84, 0.89],
      'ENG': [0.88, 0.83, 0.91, 0.86, 0.87],
      'PAK': [0.80, 0.89, 0.85, 0.90, 0.82],
    };
    
    const basePerf = performanceMap[player.team] || [0.85, 0.85, 0.85, 0.85, 0.85];
    const avgPerformance = basePerf.reduce((a, b) => a + b) / basePerf.length;
    return Math.round(avgPerformance * 100);
  };

  const generateTeam = async (teamType = 'balanced') => {
    if (players.length < 11) {
      alert('Please add at least 11 players!');
      return;
    }

    setLoading(true);
    
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 1500));

    const today = new Date();
    const analyzedPlayers = players.map(player => ({
      ...player,
      mlScore: calculateMLPrediction(player, matchDetails),
      astrologyScore: calculateAstrologyScore(player, today),
      venueScore: calculateVenueScore(player, matchDetails.pitchType, matchDetails.weather),
      h2hScore: analyzeHeadToHead(player, matchDetails.team2),
      totalScore: 0
    }));

    // Calculate total score
    analyzedPlayers.forEach(p => {
      p.totalScore = (p.mlScore * 0.35) + (p.astrologyScore * 0.15) + 
                     (p.venueScore * 0.20) + (p.h2hScore * 0.15) + 
                     (p.recentForm * 0.15);
    });

    // Team composition based on type
    let composition = { wk: 1, bat: 4, ar: 2, bowl: 4 };
    if (teamType === 'batting') composition = { wk: 1, bat: 5, ar: 2, bowl: 3 };
    if (teamType === 'bowling') composition = { wk: 1, bat: 3, ar: 2, bowl: 5 };

    // Select best players by role
    const selectedTeam = [];
    const roles = {
      'WK-Batsman': composition.wk,
      'Batsman': composition.bat,
      'All-Rounder': composition.ar,
      'Bowler': composition.bowl
    };

    Object.entries(roles).forEach(([role, count]) => {
      const rolePlayers = analyzedPlayers
        .filter(p => p.role === role)
        .sort((a, b) => b.totalScore - a.totalScore)
        .slice(0, count);
      selectedTeam.push(...rolePlayers);
    });

    // Sort by total score and select captain/vice-captain
    selectedTeam.sort((a, b) => b.totalScore - a.totalScore);
    
    const captain = selectedTeam[0];
    const viceCaptain = selectedTeam[1];

    // Calculate win probability
    const avgTeamScore = selectedTeam.reduce((sum, p) => sum + p.totalScore, 0) / selectedTeam.length;
    const winProbability = Math.min(95, Math.max(45, avgTeamScore * 1.2));
    const failureRisk = 100 - winProbability;

    // Pattern analysis
    const patterns = [
      { pattern: "Form-based dominance", confidence: 87, description: "Team heavily relies on recent form" },
      { pattern: "Astrology alignment", confidence: 76, description: `Favorable day for players with Mulank ${captain.mulank}` },
      { pattern: "Venue optimization", confidence: 82, description: `${matchDetails.pitchType} pitch favors selected composition` }
    ];

    setPredictions({
      team: selectedTeam,
      captain,
      viceCaptain,
      winProbability: winProbability.toFixed(1),
      failureRisk: failureRisk.toFixed(1),
      patterns,
      teamType,
      totalCost: selectedTeam.reduce((sum, p) => sum + p.price, 0).toFixed(1),
      megaContestPotential: winProbability > 75 ? "HIGH" : winProbability > 60 ? "MEDIUM" : "LOW"
    });

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-900 via-green-800 to-emerald-900 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-white mb-2 flex items-center justify-center gap-3">
            <Trophy className="w-12 h-12 text-yellow-400" />
            AI Fantasy Cricket Team Generator
          </h1>
          <p className="text-green-200 text-lg">ML + Astrology + Numerology + Venue Analysis</p>
        </div>

        {/* Match Details */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 mb-6 border border-white/20">
          <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
            <Activity className="w-6 h-6" />
            Match Details
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <input
              type="text"
              placeholder="Team 1"
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/60"
              value={matchDetails.team1}
              onChange={(e) => setMatchDetails({...matchDetails, team1: e.target.value})}
            />
            <input
              type="text"
              placeholder="Team 2"
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/60"
              value={matchDetails.team2}
              onChange={(e) => setMatchDetails({...matchDetails, team2: e.target.value})}
            />
            <input
              type="text"
              placeholder="Venue"
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/60"
              value={matchDetails.venue}
              onChange={(e) => setMatchDetails({...matchDetails, venue: e.target.value})}
            />
            <select
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white"
              value={matchDetails.weather}
              onChange={(e) => setMatchDetails({...matchDetails, weather: e.target.value})}
            >
              <option value="sunny">☀️ Sunny</option>
              <option value="cloudy">☁️ Cloudy</option>
              <option value="humid">💧 Humid</option>
              <option value="windy">🌪️ Windy</option>
            </select>
            <select
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white"
              value={matchDetails.pitchType}
              onChange={(e) => setMatchDetails({...matchDetails, pitchType: e.target.value})}
            >
              <option value="batting">🏏 Batting Pitch</option>
              <option value="bowling">⚡ Bowling Pitch</option>
              <option value="balanced">⚖️ Balanced Pitch</option>
            </select>
            <input
              type="number"
              placeholder="Budget (Credits)"
              className="bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/60"
              value={budget}
              onChange={(e) => setBudget(Number(e.target.value))}
            />
          </div>
        </div>

        {/* Player Input */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 mb-6 border border-white/20">
          <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
            <Users className="w-6 h-6" />
            Add Players ({players.length}/22)
          </h2>
          <div className="flex gap-3 mb-4">
            <input
              type="text"
              placeholder="Enter player name"
              className="flex-1 bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/60"
              value={playerInput}
              onChange={(e) => setPlayerInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && addPlayer()}
            />
            <button
              onClick={addPlayer}
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold transition"
            >
              Add Player
            </button>
            <button
              onClick={loadSamplePlayers}
              className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold transition"
            >
              Load Sample
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 max-h-96 overflow-y-auto">
            {players.map((player, idx) => (
              <div key={idx} className="bg-white/20 rounded-lg p-3 border border-white/20">
                <div className="flex justify-between items-start">
                  <div>
                    <p className="text-white font-bold">{player.name}</p>
                    <p className="text-green-200 text-sm">{player.team} • {player.role}</p>
                  </div>
                  <span className="bg-yellow-500 text-xs px-2 py-1 rounded font-bold">
                    {player.price}Cr
                  </span>
                </div>
                <div className="mt-2 flex gap-2 text-xs">
                  <span className="bg-blue-500/50 px-2 py-1 rounded text-white">Form: {player.recentForm}</span>
                  <span className="bg-purple-500/50 px-2 py-1 rounded text-white">M: {player.mulank}</span>
                  <span className="bg-pink-500/50 px-2 py-1 rounded text-white">B: {player.bhagyank}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Generate Team Buttons */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <button
            onClick={() => generateTeam('batting')}
            disabled={loading}
            className="bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-700 hover:to-red-700 text-white py-4 rounded-xl font-bold text-lg transition disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <Target className="w-5 h-5" />
            Batting Heavy Team
          </button>
          <button
            onClick={() => generateTeam('balanced')}
            disabled={loading}
            className="bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white py-4 rounded-xl font-bold text-lg transition disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <Award className="w-5 h-5" />
            Balanced Team
          </button>
          <button
            onClick={() => generateTeam('bowling')}
            disabled={loading}
            className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white py-4 rounded-xl font-bold text-lg transition disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <Zap className="w-5 h-5" />
            Bowling Heavy Team
          </button>
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-white mx-auto mb-4"></div>
            <p className="text-white text-xl font-semibold">Analyzing with AI + Astrology + ML...</p>
          </div>
        )}

        {/* Predictions */}
        {predictions && !loading && (
          <div className="space-y-6">
            {/* Win Probability */}
            <div className="bg-gradient-to-r from-yellow-500 to-orange-500 rounded-2xl p-6 border-4 border-yellow-300">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-3xl font-bold text-white flex items-center gap-2">
                  <TrendingUp className="w-8 h-8" />
                  AI Prediction Analysis
                </h2>
                <span className={`text-4xl font-black ${predictions.megaContestPotential === 'HIGH' ? 'text-green-900' : 'text-orange-900'}`}>
                  {predictions.megaContestPotential}
                </span>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-white/20 rounded-xl p-4">
                  <p className="text-white/80 text-sm mb-1">Win Probability</p>
                  <p className="text-4xl font-bold text-white">{predictions.winProbability}%</p>
                </div>
                <div className="bg-white/20 rounded-xl p-4">
                  <p className="text-white/80 text-sm mb-1">Failure Risk</p>
                  <p className="text-4xl font-bold text-white">{predictions.failureRisk}%</p>
                </div>
                <div className="bg-white/20 rounded-xl p-4">
                  <p className="text-white/80 text-sm mb-1">Total Cost</p>
                  <p className="text-4xl font-bold text-white">{predictions.totalCost}Cr</p>
                </div>
              </div>
            </div>

            {/* Captain & Vice Captain */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-gradient-to-br from-yellow-500 to-yellow-600 rounded-2xl p-6 border-4 border-yellow-300">
                <div className="flex items-center gap-3 mb-3">
                  <Star className="w-8 h-8 text-white fill-white" />
                  <h3 className="text-2xl font-bold text-white">CAPTAIN (2x)</h3>
                </div>
                <p className="text-3xl font-black text-white mb-2">{predictions.captain.name}</p>
                <div className="flex gap-2 flex-wrap">
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    Form: {predictions.captain.recentForm}
                  </span>
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    Score: {predictions.captain.totalScore.toFixed(1)}
                  </span>
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    {predictions.captain.role}
                  </span>
                </div>
              </div>

              <div className="bg-gradient-to-br from-gray-400 to-gray-500 rounded-2xl p-6 border-4 border-gray-300">
                <div className="flex items-center gap-3 mb-3">
                  <Star className="w-8 h-8 text-white" />
                  <h3 className="text-2xl font-bold text-white">VICE CAPTAIN (1.5x)</h3>
                </div>
                <p className="text-3xl font-black text-white mb-2">{predictions.viceCaptain.name}</p>
                <div className="flex gap-2 flex-wrap">
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    Form: {predictions.viceCaptain.recentForm}
                  </span>
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    Score: {predictions.viceCaptain.totalScore.toFixed(1)}
                  </span>
                  <span className="bg-white/30 px-3 py-1 rounded-full text-white text-sm">
                    {predictions.viceCaptain.role}
                  </span>
                </div>
              </div>
            </div>

            {/* Pattern Analysis */}
            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
              <h3 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
                <Cloud className="w-6 h-6" />
                Pattern Analysis
              </h3>
              <div className="space-y-3">
                {predictions.patterns.map((pattern, idx) => (
                  <div key={idx} className="bg-white/10 rounded-lg p-4">
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-white font-bold">{pattern.pattern}</span>
                      <span className="bg-blue-500 px-3 py-1 rounded-full text-white text-sm font-bold">
                        {pattern.confidence}% confidence
                      </span>
                    </div>
                    <p className="text-green-200 text-sm">{pattern.description}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Selected Team */}
            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
              <h3 className="text-2xl font-bold text-white mb-4">
                Final Team - {predictions.teamType.toUpperCase()}
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {predictions.team.map((player, idx) => (
                  <div key={idx} className="bg-gradient-to-br from-white/20 to-white/10 rounded-lg p-4 border border-white/30">
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <p className="text-white font-bold text-lg">{player.name}</p>
                        <p className="text-green-200 text-sm">{player.team} • {player.role}</p>
                      </div>
                      {idx === 0 && <span className="bg-yellow-500 text-xs px-2 py-1 rounded font-bold">C</span>}
                      {idx === 1 && <span className="bg-gray-400 text-xs px-2 py-1 rounded font-bold">VC</span>}
                    </div>
                    <div className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span className="text-white/70">AI Score:</span>
                        <span className="text-white font-bold">{player.totalScore.toFixed(1)}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-white/70">Form:</span>
                        <span className="text-green-300 font-bold">{player.recentForm}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-white/70">Astrology:</span>
                        <span className="text-purple-300 font-bold">{player.astrologyScore}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-white/70">Venue:</span>
                        <span className="text-blue-300 font-bold">{player.venueScore}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-white/70">H2H:</span>
                        <span className="text-orange-300 font-bold">{player.h2hScore}%</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Trophy component
const Trophy = ({ className }) => (
  <svg className={className} fill="currentColor" viewBox="0 0 24 24">
    <path d="M20 2H4c-1.1 0-2 .9-2 2v2c0 1.1.9 2 2 2h1v4c0 2.76 2.
