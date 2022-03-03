"""
api_client.py

Use Case:
Say you worked at a company that wanted twitter data, 
you would us Twitter's API to get their data

Similarly Amazon, Walmart, Spotify, Instagram, Facebook,
all have APIs
"""
import posixpath
import requests

import pandas as pd
from pprint import pprint 

from typing import List, Dict


class RickAndMortyBaseClient:

    base_url = "https://rickandmortyapi.com/api"
    endpoint = None
    
    def get_all_results(self, verbose: bool = True) -> List[Dict]:
        if self.endpoint is None:
            raise Exception("Cannot use get_all_results from base_class, must use child classes")
        url = posixpath.join(self.base_url, self.endpoint)
        response = requests.get(url)

        info = response.json()['info']
        page_number = info['pages']

        results_list = []

        for page in range(1, page_number+1):
            params = {"page": page}
            if verbose:
                print(params)
            response = requests.get(url=url, params=params)
            results = response.json()['results']
            results_list.extend(results)
        return results_list


class RickAndMortyCharacterClient(RickAndMortyBaseClient):

    endpoint = "character"
    

class RickAndMortyEpisodeClient(RickAndMortyBaseClient):
    
    endpoint = "episode"


if __name__=="__main__":
    client = RickAndMortyEpisodeClient()
    results = client.get_all_results()
    print(results)
    