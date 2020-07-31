<?php
    $PATH_TO_CSV = "../Resources/Отзывы/AppStore (за год).csv";
    $PATH_TO_RES = "../Resources/data.json";
    $i = 0;
    $res = array();
    if (($handle = fopen($PATH_TO_CSV, "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            // $num = count($data);
            // print_r($data);
            // if ($i == 2)
            $new_data = array();
            $i++;
            // print_r($data);
            if ($i < 4)
                continue;
            // $res[]
            // foreach ($data as $col) {
                $new_data['Date'] = $data[0];
                // $new_data[''] = $data[1];
                // $new_data['Date'] = $data[2];
                $new_data['Country'] = $data[3];
                $new_data['Version'] = $data[4];
                $new_data['Author'] = $data[5];
                $new_data['Rating'] = $data[6];
                $new_data['Title'] = $data[7];
                $new_data['Review'] = $data[8];
                // $new_data['Tran'] = $data[9];
                // $new_data['Date'] = $data[10];
                $new_data['Reply Date'] = $data[11];
                $new_data['Developer Reply'] = $data[12];
                $new_data['User'] = $data[13];
                $new_data['Tags'] = $data[14];
                $new_data['Categories'] = $data[15];
                $new_data['Notes'] = $data[16];
                $new_data['Likes'] = $data[17];
                $new_data['Dislikes'] = $data[18];
                // $new_data['Reply Date'] = $data[20];
                // $new_data['Reply Date'] = $data[21];
            // }

            $res[] = $new_data;
            // if ($i == 6)
            //     break;
        }
        file_put_contents($PATH_TO_RES, json_encode($res));
    }
?>
