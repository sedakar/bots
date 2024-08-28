from google.cloud import recommender_v1


def get_recommendations(project_entire_name, recommender, location):
    client = recommender_v1.RecommenderClient()
    parent = client.recommender_path(project_entire_name, location, recommender)
    request = recommender_v1.ListRecommendationsRequest(parent=parent)
    response = client.list_recommendations(request=request)

    return response

if __name__ == "__main__":

    project_entire_name = ""
    recommender = ""
    location = ""

    get_recommendations(project_entire_name, recommender, location)