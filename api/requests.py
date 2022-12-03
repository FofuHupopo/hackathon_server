import requests
from dadata import Dadata
from pprint import pprint


class DadataAddressSearch:
    TOKEN = "48ab36191d6ef5b11a3ae58d406b7d641a1fbd32"
    DADATA = Dadata(TOKEN)
    REQUIRED_VALUES = (
        ()
    )
    
    def search(search: str, limit: int = None):
        result = DadataAddressSearch.DADATA.suggest("address", search)
        
        if not result:
            return None
        
        response = [
            res.get("value")
            for res in result
        ]
        
        if limit:
            response = response[:limit]
        
        return response
    
    def get(address: str):
        result = DadataAddressSearch.DADATA.suggest("address", address)

        if not result:
            return None
        
        result = result[0]
        
        pprint(result)
        
        region = result.get("data", {}).get("region", "")
        region_type = result.get("data", {}).get("region_type_full", "")
        
        if region_type == "область":
            region = f"{region} {region_type}".capitalize()
        elif region_type == "республика":
            region = f"{region_type} {region}".title()
        elif region_type == "автономный округ":
            region = region.replace("Автономный округ", "АО")
            
        return {
            "county": result.get("data", {}).get("country"),
            "region": region,
            "area": result.get("data", {}).get("area"),
            "city": result.get("data", {}).get("city"),
            "street": result.get("data", {}).get("street"),
            "number": result.get("data", {}).get("house"),
            "corpus": result.get("data", {}).get("block"),
            "flat_number": result.get("data", {}).get("flat")
        }


if __name__ == "__main__":
    pprint(DadataAddressSearch.search("Оренбург Монтажников 23"))
