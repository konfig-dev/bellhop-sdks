from bellhop.paths.pet_pet_id.get import ApiForget
from bellhop.paths.pet_pet_id.post import ApiForpost
from bellhop.paths.pet_pet_id.delete import ApiFordelete


class PetPetId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
