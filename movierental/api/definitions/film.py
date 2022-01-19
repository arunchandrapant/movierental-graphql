import strawberry
from typing import List, Optional


@strawberry.type(description="A film and it's attributes")
class Film:
    film_id: int
    title: str
    description: str
    release_year: int
    language: str
    original_language: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    mpaa_rating: str

    import movierental.api.definitions.actor as actordf

    @strawberry.field(description="Actors in the film")
    def actor(self) -> Optional[List[actordf.Actor]]:
        import movierental.database.dataaccess.film as FilmDA
        import movierental.database.dataaccess.actor as ActorDA

        actor_ids = FilmDA.get_actors_for_a_film(self.film_id)
        return ActorDA.get_actor(actor_ids)

    @classmethod
    def from_instance(cls, instance):
        return cls(
            film_id=instance.film_id,
            title=instance.title,
            description=instance.description,
            release_year=instance.release_year,
            language=instance.language.name,
            original_language=instance.original_language,
            rental_duration=instance.rental_duration,
            rental_rate=instance.rental_rate,
            length=instance.length,
            replacement_cost=instance.replacement_cost,
            mpaa_rating=instance.rating,
        )
