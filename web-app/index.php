<?php

$command = 'python svm.py NaCl';
exec($command, $out, $status);
print_r($out);

?>
