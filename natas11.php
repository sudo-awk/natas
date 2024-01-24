#!/usr/bin/php8.2
<?php

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in,$key) {
    $text = $in; 
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$key = 'KNHL';

$ciphertext = base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=');

$good_data= json_encode($defaultdata);

echo xor_encrypt($good_data,$key);
//this is the result when piped with base64 encode 'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz'

?>
