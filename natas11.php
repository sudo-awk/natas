#!/usr/bin/php8.2
<?php



function xor_encrypt($in) {
    $key = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
    $text = $in; 
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$plaintext = array( "showpassword"=>"no", "bgcolor"=>"#ffffff" );
$cookie =base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=');
echo $cookie;

print  base64_encode($plaintext);

?>
