from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def build_model():
    model = DiscreteBayesianNetwork([
        ('UserAge', 'GenrePreference'),
        ('UserGender', 'GenrePreference'),
        ('GenrePreference', 'LikedMovie'),
        ('MovieGenre', 'LikedMovie')
    ])

    cpd_user_age = TabularCPD(variable='UserAge', variable_card=2, values=[[0.5], [0.5]])
    cpd_user_gender = TabularCPD(variable='UserGender', variable_card=3, values=[[1/3], [1/3], [1/3]])
    cpd_genre_pref = TabularCPD(variable='GenrePreference', variable_card=3,
                                 values=[[0.6, 0.3, 0.4, 0.2, 0.3, 0.1],
                                         [0.3, 0.5, 0.4, 0.5, 0.4, 0.3],
                                         [0.1, 0.2, 0.2, 0.3, 0.3, 0.6]],
                                 evidence=['UserAge', 'UserGender'],
                                 evidence_card=[2, 3])

    cpd_movie_genre = TabularCPD(variable='MovieGenre', variable_card=6,
                                  values=[[1/6], [1/6], [1/6], [1/6], [1/6], [1/6]])

    cpd_liked_movie = TabularCPD(variable='LikedMovie', variable_card=2,
                                  values=[[0.7, 0.4, 0.6, 0.5, 0.3, 0.2, 0.6, 0.7, 0.3, 0.5, 0.6, 0.4, 0.2, 0.3, 0.1, 0.5, 0.7, 0.4],
                                          [0.3, 0.6, 0.4, 0.5, 0.7, 0.8, 0.4, 0.3, 0.7, 0.5, 0.4, 0.6, 0.8, 0.7, 0.9, 0.5, 0.3, 0.6]],
                                  evidence=['GenrePreference', 'MovieGenre'],
                                  evidence_card=[3, 6])

    model.add_cpds(cpd_user_age, cpd_user_gender, cpd_genre_pref, cpd_movie_genre, cpd_liked_movie)
    return VariableElimination(model)

def get_prediction(infer, age, gender, genre):
    evidence = {"UserAge": age, "UserGender": gender, "MovieGenre": genre}  # Match node names
    result = infer.query(variables=["LikedMovie"], evidence=evidence)  # Query LikedMovie
    return result


def get_probabilities(inference, age, gender, genre):
    result = inference.query(variables=["LikedMovie"], evidence={
        "UserAge": age,
        "UserGender": gender,
        "MovieGenre": genre
    }, show_progress=False)
    return {"No": float(result.values[0]), "Yes": float(result.values[1])}
