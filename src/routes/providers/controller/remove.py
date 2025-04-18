from services.providers.delete import delete_provider


async def remove_provider(provider_id: int):
    res = await delete_provider(provider_id)
    print(res, "RES")
    return {"message": "Provider deleted successfully"}
