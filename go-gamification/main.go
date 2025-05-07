package main

import (
	"encoding/json"
	"log"
	"net/http"
	"sort"
	"sync"
)

type Workout struct {
	UserID      int     `json:"user_id"`
	WorkoutType string  `json:"workout_type"`
	Duration    float64 `json:"duration"`
	Intensity   string  `json:"intensity"`
	Notes       string  `json:"notes"`
	XP          int     `json:"xp"`
}

type Leaderboard struct {
	UserID int `json:"user_id"`
	XP     int `json:"xp"`
}

var leaderboardData []Leaderboard
var mu sync.Mutex

// Calculate XP based on workout type and intensity
func calculateXP(workout Workout) int {
	xpMap := map[string]map[string]int{
		"Running": {"Low": 10, "Medium": 20, "High": 30},
		"Cycling": {"Low": 8, "Medium": 16, "High": 24},
		"Weights": {"Low": 12, "Medium": 24, "High": 36},
		"Yoga":    {"Low": 5, "Medium": 10, "High": 15},
	}
	return xpMap[workout.WorkoutType][workout.Intensity]
}

// POST /log-workout
func logWorkout(w http.ResponseWriter, r *http.Request) {
	var workout Workout
	err := json.NewDecoder(r.Body).Decode(&workout)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	workout.XP = calculateXP(workout)

	mu.Lock()
	leaderboardData = append(leaderboardData, Leaderboard{
		UserID: workout.UserID,
		XP:     workout.XP,
	})
	mu.Unlock()

	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(workout)
}

// GET /leaderboard
func leaderboardHandler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()

	sort.Slice(leaderboardData, func(i, j int) bool {
		return leaderboardData[i].XP > leaderboardData[j].XP
	})

	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(leaderboardData)
}

func main() {
	http.HandleFunc("/log-workout", logWorkout)
	http.HandleFunc("/leaderboard", leaderboardHandler)

	log.Println("Go service is running on port 9000")
	err := http.ListenAndServe(":9000", nil)
	if err != nil {
		log.Fatal(err)
	}
}
