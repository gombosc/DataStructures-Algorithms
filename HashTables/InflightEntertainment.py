flight_length = 260
movie_lengths = [120, 140, 180, 200]

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            print("Movies match flight length")
            return True
        movie_lengths_seen.add(first_movie_length)
        
        # We never found a match, so return False
    print("No movies match")
    return False

# Complexity: O(n) time, and O(n) space. Note while optimizing runtime we added a bit of space cost.

# What We Learned
# The trick was to use a set to access our movies by length, in O(1) time.
# Using hash-based data structures, like dictionaries or sets, is so common in coding challenge solutions, it should always be your first thought. Always ask yourself, right from the start: "Can I save time by using a dictionary?"

can_two_movies_fill_flight(movie_lengths, flight_length)