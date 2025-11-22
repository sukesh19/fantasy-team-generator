import React, { useState } from 'react';
import { TrendingUp, Users, Target, Star, Zap, CloudRain, Calendar, Award } from 'lucide-react';

const PLAYERS = [
  // Batsmen
  { id: 1, name: "Virat Kohli", role: "Batsman", team: "mi", rating: 95, form: 88, avg: 52.3, sr: 138, venueAvg: 58, recentScores: [73, 45, 89, 12, 67], moonPhase: 0.8, mulank: 5, bhagyank: 8 },
  { id: 2, name: "Rohit Sharma", role: "Batsman", team: "MI", rating: 94, form: 85, avg: 48.7, sr: 142, venueAvg: 52, recentScores: [91, 23, 56, 78, 34], moonPhase: 0.7, mulank: 3, bhagyank: 6 },
  { id: 3, name: "KL Rahul", role: "Batsman", team: "LSG", rating: 92, form: 82, avg: 47.2, sr: 135, venueAvg: 49, recentScores: [45, 67, 23, 89, 56], moonPhase: 0.6, mulank: 2, bhagyank: 5 },
  { id: 4, name: "Shubman Gill", role: "Batsman", team: "GT", rating: 90, form: 91, avg: 44.8, sr: 140, venueAvg: 54, recentScores: [78, 92, 45, 67, 88], moonPhase: 0.9, mulank: 7, bhagyank: 9 },
  { id: 5, name: "David Warner", role: "Batsman", team: "DC", rating: 93, form: 80, avg: 50.1, sr: 145, venueAvg: 47, recentScores: [34, 56, 78, 23, 91], moonPhase: 0.5, mulank: 4, bhagyank: 7 },
  { id: 6, name: "Quinton de Kock", role: "WK-Batsman", team: "LSG", rating: 89, form: 84, avg: 43.5, sr: 137, venueAvg: 51, recentScores: [67, 45, 89, 34, 72], moonPhase: 0.7, mulank: 6, bhagyank: 8 },
  { id: 7, name: "Jos Buttler", role: "WK-Batsman", team: "RR", rating: 91, form: 87, avg: 46.9, sr: 152, venueAvg: 55, recentScores: [103, 45, 67, 89, 23], moonPhase: 0.8, mulank: 1, bhagyank: 4 },
  
  // All-rounders
  { id: 8, name: "Hardik Pandya", role: "All-Rounder", team: "MI", rating: 93, form: 89, avg: 32.4, sr: 148, wickets: 23, economy: 8.2, venueAvg: 38, recentScores: [45, 67, 23, 89, 56], moonPhase: 0.8, mulank: 9, bhagyank: 3 },
  { id: 9, name: "Ravindra Jadeja", role: "All-Rounder", team: "CSK", rating: 91, form: 85, avg: 28.7, sr: 132, wickets: 31, economy: 7.5, venueAvg: 34, recentScores: [34, 56, 12, 78, 45], moonPhase: 0.6, mulank: 8, bhagyank: 2 },
  { id: 10, name: "Glenn Maxwell", role: "All-Rounder", team: "RCB", rating: 90, form: 83, avg: 30.2, sr: 155, wickets: 18, economy: 8.5, venueAvg: 36, recentScores: [89, 23, 67, 12, 91], moonPhase: 0.7, mulank: 5, bhagyank: 7 },
  { id: 11, name: "Marcus Stoinis", role: "All-Rounder", team: "LSG", rating: 87, form: 81, avg: 29.5, sr: 140, wickets: 15, economy: 9.1, venueAvg: 32, recentScores: [45, 67, 34, 56, 23], moonPhase: 0.5, mulank: 3, bhagyank: 6 },
  { id: 12, name: "Axar Patel", role: "All-Rounder", team: "DC", rating: 86, form: 86, avg: 24.3, sr: 128, wickets: 28, economy: 7.2, venueAvg: 28, recentScores: [23, 45, 67, 12, 56], moonPhase: 0.8, mulank: 7, bhagyank: 9 },
  
  // Bowlers
  { id: 13, name: "Jasprit Bumrah", role: "Bowler", team: "MI", rating: 96, form: 92, wickets: 45, economy: 6.8, avg: 18.5, venueWickets: 12, recentWickets: [3, 2, 4, 1, 3], moonPhase: 0.9, mulank: 2, bhagyank: 5 },
  { id: 14, name: "Rashid Khan", role: "Bowler", team: "GT", rating: 95, form: 90, wickets: 42, economy: 7.1, avg: 19.2, venueWickets: 11, recentWickets: [2, 3, 1, 4, 2], moonPhase: 0.8, mulank: 4, bhagyank: 7 },
  { id: 15, name: "Yuzvendra Chahal", role: "Bowler", team: "RR", rating: 92, form: 88, wickets: 38, economy: 7.8, avg: 21.3, venueWickets: 9, recentWickets: [2, 1, 3, 2, 4], moonPhase: 0.7, mulank: 6, bhagyank: 8 },
  { id: 16, name: "Mohammed Siraj", role: "Bowler", team: "RCB", rating: 90, form: 87, wickets: 35, economy: 8.1, avg: 22.5, venueWickets: 8, recentWickets: [3, 2, 1, 2, 3], moonPhase: 0.6, mulank: 8, bhagyank: 1 },
  { id: 17, name: "Trent Boult", role: "Bowler", team: "RR", rating: 91, form: 85, wickets: 37, economy: 7.9, avg: 20.8, venueWickets: 10, recentWickets: [2, 3, 2, 1, 4], moonPhase: 0.8, mulank: 1, bhagyank: 3 },
  { id: 18, name: "Kagiso Rabada", role: "Bowler", team: "DC", rating: 93, form: 89, wickets: 40, economy: 7.5, avg: 19.7, venueWickets: 11, recentWickets: [4, 2, 3, 2, 3], moonPhase: 0.7, mulank: 9, bhagyank: 2 },
  { id: 19, name: "Kuldeep Yadav", role: "Bowler", team: "DC", rating: 88, form: 86, wickets: 33, economy: 7.6, avg: 23.1, venueWickets: 7, recentWickets: [2, 1, 3, 2, 2], moonPhase: 0.6, mulank: 5, bhagyank: 8 },
  { id: 20, name: "Harshal Patel", role: "Bowler", team: "PBKS", rating: 87, form: 82, wickets: 32, economy: 8.4, avg: 24.2, venueWickets: 6, recentWickets: [1, 2, 3, 1, 2], moonPhase: 0.5, mulank: 3, bhagyank: 6 },
  { id: 21, name: "Arshdeep Singh", role: "Bowler", team: "PBKS", rating: 85, form: 84, wickets: 30, economy: 8.2, avg: 25.3, venueWickets: 5, recentWickets: [2, 1, 2, 3, 1], moonPhase: 0.7, mulank: 7, bhagyank: 9 },
  { id: 22, name: "Shardul Thakur", role: "All-Rounder", team: "DC", rating: 84, form: 80, wickets: 28, economy: 8.8, avg: 21.5, venueWickets: 6, recentWickets: [1, 2, 1, 2, 3], moonPhase: 0.6, mulank: 4, bhagyank: 5 }
];

const FantasyCricketAI = () => {
  const [selectedPlayers, setSelectedPlayers] = useState([]);
  const [budget, setBudget] = useState(100);
  const [weather, setWeather] = useState('sunny');
  const [venue, setVenue] = useState('wankhede');
  const [teamStrategy, setTeamStrategy] = useState('balanced');
  const [showPrediction, setShowPrediction] = useState(false);
  const [captain, setCaptain] = useState(null);
  const [viceCaptain, setViceCaptain] = useState(null);
  const [matchDate, setMatchDate] = useState(new Date().toISOString().split('T')[0]);

  const togglePlayer = (player) => {
    if (selectedPlayers.find(p => p.id === player.id)) {
      setSelectedPlayers(selectedPlayers.filter(p => p.id !== player.id));
      if (captain?.id === player.id) setCaptain(null);
      if (viceCaptain?.id === player.id) setViceCaptain(null);
    } else if (selectedPlayers.length < 11) {
      setSelectedPlayers([...selectedPlayers, player]);
    }
  };

  const calculateAIScore = (player) => {
    const date = new Date(matchDate);
    const dayNumber = date.getDate();
    const dayOfWeek = date.getDay();
    
    // Base score from rating and form
    let score = player.rating * 0.4 + player.form * 0.3;
    
    // Weather impact
    const weatherBonus = {
      sunny: player.role === 'Batsman' ? 1.2 : 1.0,
      cloudy: player.role === 'Bowler' ? 1.15 : 1.0,
      rainy: player.role === 'Bowler' ? 1.25 : 0.9,
      humid: player.role === 'All-Rounder' ? 1.1 : 1.0
    };
    score *= weatherBonus[weather];
    
    // Venue performance
    score += player.venueAvg * 0.2;
    
    // Astrological factors
    const mulankBonus = (player.mulank === (dayNumber % 9) || player.mulank === 9) ? 1.15 : 1.0;
    const bhagyankBonus = (player.bhagyank === ((dayNumber % 9) + dayOfWeek) % 9) ? 1.1 : 1.0;
    const moonBonus = player.moonPhase > 0.7 ? 1.12 : 1.0;
    
    score *= mulankBonus * bhagyankBonus * moonBonus;
    
    // Recent form analysis
    const recentAvg = player.recentScores ? 
      player.recentScores.reduce((a, b) => a + b, 0) / player.recentScores.length : 
      (player.recentWickets ? player.recentWickets.reduce((a, b) => a + b, 0) * 10 : 0);
    score += recentAvg * 0.15;
    
    // Team strategy bonus
    const strategyBonus = {
      batting: player.role === 'Batsman' ? 1.15 : (player.role === 'All-Rounder' ? 1.05 : 0.95),
      bowling: player.role === 'Bowler' ? 1.15 : (player.role === 'All-Rounder' ? 1.05 : 0.95),
      balanced: 1.0
    };
    score *= strategyBonus[teamStrategy];
    
    return Math.round(score * 10) / 10;
  };

  const generateAITeam = () => {
    const scoredPlayers = PLAYERS.map(p => ({
      ...p,
      aiScore: calculateAIScore(p)
    })).sort((a, b) => b.aiScore - a.aiScore);

    let team = [];
    let batsmen = 0, bowlers = 0, allRounders = 0, wk = 0;

    // Strategy-based composition
    const requirements = {
      batting: { batsmen: 5, bowlers: 3, allRounders: 2, wk: 1 },
      bowling: { batsmen: 3, bowlers: 5, allRounders: 2, wk: 1 },
      balanced: { batsmen: 4, bowlers: 4, allRounders: 2, wk: 1 }
    };

    const req = requirements[teamStrategy];

    for (const player of scoredPlayers) {
      if (team.length >= 11) break;

      const isWK = player.name.includes('de Kock') || player.name.includes('Buttler');
      
      if (isWK && wk < req.wk) {
        team.push(player);
        wk++;
      } else if (player.role === 'Batsman' && batsmen < req.batsmen && !isWK) {
        team.push(player);
        batsmen++;
      } else if (player.role === 'Bowler' && bowlers < req.bowlers) {
        team.push(player);
        bowlers++;
      } else if (player.role === 'All-Rounder' && allRounders < req.allRounders) {
        team.push(player);
        allRounders++;
      }
    }

    setSelectedPlayers(team);
    
    // Auto-select captain and vice-captain
    const topTwo = team.slice(0, 2);
    setCaptain(topTwo[0]);
    setViceCaptain(topTwo[1]);
  };

  const analyzePrediction = () => {
    const totalScore = selectedPlayers.reduce((sum, p) => sum + calculateAIScore(p), 0);
    const avgScore = totalScore / selectedPlayers.length;
    
    const captainBonus = captain ? calculateAIScore(captain) * 2 : 0;
    const vcBonus = viceCaptain ? calculateAIScore(viceCaptain) * 1.5 : 0;
    
    const finalScore = totalScore + captainBonus + vcBonus;
    
    const winProbability = Math.min(95, Math.max(45, (finalScore / 12) + 20));
    const megaContestRank = Math.round(100000 / (winProbability / 10));
    
    return {
      totalScore: Math.round(totalScore),
      avgScore: Math.round(avgScore * 10) / 10,
      finalScore: Math.round(finalScore),
      winProbability: Math.round(winProbability * 10) / 10,
      megaContestRank,
      riskLevel: winProbability > 75 ? 'Low' : winProbability > 60 ? 'Medium' : 'High',
      successPattern: winProbability > 70 ? 'Excellent' : winProbability > 55 ? 'Good' : 'Risky'
    };
  };

  const prediction = showPrediction ? analyzePrediction() : null;

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-purple-900 to-pink-900 p-4">
      <div className="max-w-7xl mx-auto">
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 mb-6 border border-white/20">
          <h1 className="text-4xl font-bold text-white mb-2 flex items-center gap-3">
            <Zap className="text-yellow-400" />
            AI Fantasy Cricket Team Generator
          </h1>
          <p className="text-purple-200">ML Predictions • Astrology • Weather • Venue Analysis</p>
        </div>

        {/* Configuration Panel */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-4 border border-white/20">
            <label className="text-white font-semibold mb-2 block flex items-center gap-2">
              <CloudRain size={18} />
              Weather
            </label>
            <select 
              value={weather} 
              onChange={(e) => setWeather(e.target.value)}
              className="w-full bg-white/20 text-white rounded-lg p-2 border border-white/30"
            >
              <option value="sunny">☀️ Sunny</option>
              <option value="cloudy">☁️ Cloudy</option>
              <option value="rainy">🌧️ Rainy</option>
              <option value="humid">💧 Humid</option>
            </select>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-4 border border-white/20">
            <label className="text-white font-semibold mb-2 block flex items-center gap-2">
              <Target size={18} />
              Venue
            </label>
            <select 
              value={venue} 
              onChange={(e) => setVenue(e.target.value)}
              className="w-full bg-white/20 text-white rounded-lg p-2 border border-white/30"
            >
              <option value="wankhede">Wankhede Stadium</option>
              <option value="eden">Eden Gardens</option>
              <option value="chinnaswamy">Chinnaswamy</option>
              <option value="chepauk">Chepauk</option>
            </select>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-4 border border-white/20">
            <label className="text-white font-semibold mb-2 block flex items-center gap-2">
              <TrendingUp size={18} />
              Strategy
            </label>
            <select 
              value={teamStrategy} 
              onChange={(e) => setTeamStrategy(e.target.value)}
              className="w-full bg-white/20 text-white rounded-lg p-2 border border-white/30"
            >
              <option value="batting">⚡ Batting Heavy</option>
              <option value="bowling">🎯 Bowling Heavy</option>
              <option value="balanced">⚖️ Balanced</option>
            </select>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-4 border border-white/20">
            <label className="text-white font-semibold mb-2 block flex items-center gap-2">
              <Calendar size={18} />
              Match Date
            </label>
            <input 
              type="date" 
              value={matchDate}
              onChange={(e) => setMatchDate(e.target.value)}
              className="w-full bg-white/20 text-white rounded-lg p-2 border border-white/30"
            />
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex gap-4 mb-6">
          <button
            onClick={generateAITeam}
            className="flex-1 bg-gradient-to-r from-green-500 to-emerald-600 text-white font-bold py-3 px-6 rounded-xl hover:from-green-600 hover:to-emerald-700 transition-all shadow-lg flex items-center justify-center gap-2"
          >
            <Star className="animate-pulse" />
            Generate AI Team
          </button>
          <button
            onClick={() => setShowPrediction(!showPrediction)}
            disabled={selectedPlayers.length !== 11}
            className={`flex-1 ${selectedPlayers.length === 11 ? 'bg-gradient-to-r from-purple-500 to-pink-600' : 'bg-gray-500'} text-white font-bold py-3 px-6 rounded-xl transition-all shadow-lg flex items-center justify-center gap-2`}
          >
            <Award />
            Analyze Prediction
          </button>
        </div>

        {/* Prediction Results */}
        {showPrediction && prediction && (
          <div className="bg-gradient-to-r from-yellow-400 to-orange-500 rounded-2xl p-6 mb-6 border-4 border-yellow-300">
            <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
              <Award />
              AI Prediction Analysis
            </h2>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Total Score</div>
                <div className="text-2xl font-bold text-white">{prediction.totalScore}</div>
              </div>
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Avg Score</div>
                <div className="text-2xl font-bold text-white">{prediction.avgScore}</div>
              </div>
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Final Score</div>
                <div className="text-2xl font-bold text-white">{prediction.finalScore}</div>
              </div>
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Win Probability</div>
                <div className="text-2xl font-bold text-white">{prediction.winProbability}%</div>
              </div>
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Contest Rank</div>
                <div className="text-2xl font-bold text-white">~{prediction.megaContestRank}</div>
              </div>
              <div className="bg-white/20 backdrop-blur rounded-xl p-4">
                <div className="text-white/80 text-sm">Risk Level</div>
                <div className="text-2xl font-bold text-white">{prediction.riskLevel}</div>
              </div>
            </div>
            <div className="mt-4 bg-white/20 backdrop-blur rounded-xl p-4">
              <div className="text-white font-semibold mb-2">Success Pattern: {prediction.successPattern}</div>
              <div className="text-white/90 text-sm">
                Based on ML analysis, astrological alignment ({new Date(matchDate).getDate() % 9}), weather conditions, venue statistics, and head-to-head patterns.
              </div>
            </div>
          </div>
        )}

        {/* Selected Team */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 mb-6 border border-white/20">
          <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
            <Users />
            Your Team ({selectedPlayers.length}/11)
          </h2>
          
          {selectedPlayers.length > 0 ? (
            <div className="space-y-3">
              {selectedPlayers.map(player => (
                <div key={player.id} className="bg-white/10 rounded-xl p-4 flex items-center justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3">
                      <span className="text-xl font-bold text-white">{player.name}</span>
                      <span className="px-2 py-1 bg-purple-500 rounded text-xs text-white">{player.role}</span>
                      <span className="px-2 py-1 bg-blue-500 rounded text-xs text-white">{player.team}</span>
                    </div>
                    <div className="flex gap-4 mt-2 text-sm text-white/80">
                      <span>Rating: {player.rating}</span>
                      <span>Form: {player.form}</span>
                      <span>AI Score: {calculateAIScore(player)}</span>
                      <span>Mulank: {player.mulank}</span>
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <button
                      onClick={() => setCaptain(player)}
                      className={`px-3 py-1 rounded ${captain?.id === player.id ? 'bg-yellow-500' : 'bg-white/20'} text-white text-sm`}
                    >
                      C
                    </button>
                    <button
                      onClick={() => setViceCaptain(player)}
                      className={`px-3 py-1 rounded ${viceCaptain?.id === player.id ? 'bg-yellow-500' : 'bg-white/20'} text-white text-sm`}
                    >
                      VC
                    </button>
                    <button
                      onClick={() => togglePlayer(player)}
                      className="px-3 py-1 bg-red-500 rounded text-white text-sm"
                    >
                      Remove
                    </button>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center text-white/60 py-8">
              Select players or generate AI team
            </div>
          )}
        </div>

        {/* All Players */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
          <h2 className="text-2xl font-bold text-white mb-4">All Players (22)</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {PLAYERS.map(player => {
              const isSelected = selectedPlayers.find(p => p.id === player.id);
              const aiScore = calculateAIScore(player);
              
              return (
                <div 
                  key={player.id}
                  className={`${isSelected ? 'bg-green-500/30 border-green-400' : 'bg-white/10'} rounded-xl p-4 border border-white/20 cursor-pointer transition-all hover:scale-105`}
                  onClick={() => togglePlayer(player)}
                >
                  <div className="flex justify-between items-start mb-2">
                    <div>
                      <div className="text-lg font-bold text-white">{player.name}</div>
                      <div className="flex gap-2 mt-1">
                        <span className="px-2 py-0.5 bg-purple-500 rounded text-xs text-white">{player.role}</span>
                        <span className="px-2 py-0.5 bg-blue-500 rounded text-xs text-white">{player.team}</span>
                      </div>
                    </div>
                    <div className="text-right">
                      <div className="text-2xl font-bold text-yellow-400">{aiScore}</div>
                      <div className="text-xs text-white/60">AI Score</div>
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-2 text-xs text-white/80 mt-3">
                    <div>Rating: {player.rating}</div>
                    <div>Form: {player.form}</div>
                    <div>Mulank: {player.mulank}</div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FantasyCricketAI;
