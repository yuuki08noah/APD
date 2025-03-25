from ch02.model import Champion, RoleEnum

champions: list[Champion] = [
    Champion(
        id=1,
        name="베인",
        release_date="2010-05-11",
        role=RoleEnum.MAGE
    ),
    Champion(
        id=2,
        name="고래밥",
        release_date="2025-05-05",
        role=RoleEnum.MAGE
    )
]

def getChampions():
    return champions