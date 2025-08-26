import requests
from lxml import html
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class CharacterPosition:
    column: int
    row: int
    symbol: str

class DocumentDecoder:
    def __init__(self, document_url: str):
        self.url = document_url
        self.character_positions: List[CharacterPosition] = []
        self.canvas: List[List[str]] = []
    
    def fetch_document(self) -> None:
        """Retrieve and parse the document content"""
        page_content = requests.get(self.url).content
        self._parse_document(page_content)
    
    def _parse_document(self, content: bytes) -> None:
        """Extract character positions from the document"""
        document_tree = html.fromstring(content)
        table_rows = document_tree.xpath('//table/tr[position()>1]')
        
        for row in table_rows:
            cells = row.xpath('./td')
            position = CharacterPosition(
                column=int(cells[0].text_content().strip()),
                row=int(cells[2].text_content().strip()),
                symbol=cells[1].text_content().strip()
            )
            self.character_positions.append(position)
    
    def _initialize_canvas(self) -> None:
        """Create an empty canvas with appropriate dimensions"""
        max_col = max(pos.column for pos in self.character_positions)
        max_row = max(pos.row for pos in self.character_positions)
        self.canvas = [[' ' for _ in range(max_col + 1)] for _ in range(max_row + 1)]
    
    def _place_characters(self) -> None:
        """Place characters on the canvas according to their positions"""
        for pos in self.character_positions:
            self.canvas[pos.row][pos.column] = pos.symbol
    
    def reveal_message(self) -> None:
        """Process the document and display the hidden message"""
        self.fetch_document()
        self._initialize_canvas()
        self._place_characters()
        
        # Display the message from bottom to top
        for row in reversed(self.canvas):
            print(''.join(row))

def main():
    document_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    decoder = DocumentDecoder(document_url)
    decoder.reveal_message()

if __name__ == "__main__":
    main()