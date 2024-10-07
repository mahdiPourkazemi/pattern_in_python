import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        ...


class BaseRecommendationModel(Prototype):
    def __init__(self):
        self.recommendations = ["Action Movie 1", "Comedy Movie 1"]

    def show_recommendations(self):
        print(self.recommendations)

    def clone(self) -> "BaseRecommendationModel":
        return copy.deepcopy(self)
    
if __name__=="__main__":
    user1 = BaseRecommendationModel()
    user1.recommendations.append("Action Movie 2")
    user1.show_recommendations()
    
    user2 = user1.clone()
    user2.recommendations.remove("Action Movie 2")
    user2.recommendations.append("Comedy Movie 2")
    user2.show_recommendations()