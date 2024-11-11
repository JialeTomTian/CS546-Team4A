function foundPerson(array $people): string
{
    foreach ($people as $person) {
        if ($person === 'Don') {
            return 'Don';
        }

        if ($person === 'John') {
            return 'John';
        }

        if ($person === 'Kent') {
            return 'Kent';
        }
    }

    return '';
}