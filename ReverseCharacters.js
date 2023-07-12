characters = ['a', 'b', 'c', 'd', 'e'];

const reverseCharacters = (characters) => {
    left_index = 0;
    right_index = characters.length - 1;

    while(left_index < right_index){
        let temp = characters[left_index]
        characters[left_index] = characters[right_index];
        characters[right_index] = temp;

        left_index += 1;
        right_index -= 1;
    }
    console.log(characters);
}

reverseCharacters(characters);