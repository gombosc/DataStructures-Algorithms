const flight_length = 260;
const movie_lengths = [120, 140, 180, 200];

function canTwoMoviesFillFlight (flight_length, movie_lengths){
    const moviesSeenLengths = new Set();

    for( let i=0; i < movie_lengths.length; i++){
        const firstMovieLength = movie_lengths[i];

        const matchedSecondMovie = flight_length - firstMovieLength;
        if (moviesSeenLengths.has(matchedSecondMovie)){
            console.log("Found movies for flight");
            return true
        }
        moviesSeenLengths.add(firstMovieLength);
    }

    console.log("No movies matched");
    return false
} 

canTwoMoviesFillFlight(flight_length, movie_lengths)