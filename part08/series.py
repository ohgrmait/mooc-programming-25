# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        output = f"{self.title} ({self.seasons} seasons)\n"
        output += f"genres: {", ".join(self.genres)}\n"
        if len(self.ratings) > 0:
            output += f"{len(self.ratings)} ratings, average {sum(self.ratings)/len(self.ratings):.1f} points"
        else:
            output += "no ratings"
        return output
    
    def rate(self, rating: int):
        if rating < 0 or rating > 5:
            raise ValueError("Only values between 0 and 5 are allowed")
        self.ratings.append(rating)

def minimum_grade(rating: float, series_list: list) -> list:
    desired_series = []
    for series in series_list:
        if series.ratings[0] >= rating:
            desired_series.append(series)
    return desired_series

def includes_genre(genre: str, series_list: list) -> list:
    desired_series = []
    for series in series_list:
        if genre in series.genres:
            desired_series.append(series)
    return desired_series

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
