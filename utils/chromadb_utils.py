def calculate_chunk_id(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        current_page_id = f"{chunk.metadata.get('source')}:{chunk.metadata.get('page')}"
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0
        
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        chunk.metadata["ids"] = chunk_id

    return chunks