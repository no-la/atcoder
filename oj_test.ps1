function Test {
    param (
        [Parameter(Mandatory=$true)]
        [string]$test_directory,
        [Parameter(Mandatory=$true)]
        [string]$atcoder_url,
        [Parameter(Mandatory=$true)]
        [string]$solved_file_extension
    )

    # Check if the test directory already exists
    if (Test-Path $test_directory -PathType Container) {
        Write-Host "Test directory already exists. Skipping download."
    } else {
        # Download the test cases for the specific AtCoder problem
        oj dl -d $test_directory $atcoder_url
    }

    if ($solved_file_extension -eq "cpp") {
        # Compile the C++ code using g++ with specified options and output directory
        $compiler_options = "-std=c++20 -g -Wall -Wextra -Wshadow -Wfloat-equal -Wno-char-subscripts -ftrapv -fno-omit-frame-pointer -fno-sanitize-recover"
        $compiled_output =  Join-Path (Get-Item $solved_file_path).Directory "$solved_file_name.out"
        Write-Host "Output executable path: $compiled_output"
        $command = "g++ $compiler_options -o $compiled_output $solved_file_path"

        # Execute the compilation command
        Invoke-Expression $command

        # Check if the compilation was successful
        if($LASTEXITCODE -ne 0) {
            Write-Host "Compilation failed."
            exit
        }
        # Run tests using the compiled C++ executable
        oj t -c $compiled_output -d $test_directory

        # Remove the compiled executable after testing
        Remove-Item $compiled_output -Force
    } elseif ($solved_file_extension -eq "py") {
        # Run tests using the provided Python script
        oj test -c "pypy3 $solved_file_path" -d $test_directory
    } else {
        Write-Host "Unsupported file extension: $solved_file_extension"
    }
}

function Submmit{
    param (
        [Parameter(Mandatory=$true)]
        [string]$atcoder_url,
        [Parameter(Mandatory=$true)]
        [string]$solved_file_path,
        [Parameter(Mandatory=$true)]
        [string]$solved_file_extension
    )

    if ($LASTEXITCODE -eq 0) {
        $result = "OK"
    } else {
        $result = "NG"
    }
    Write-Host "Result: $result"
    if($result -ne "OK") {
        exit
    }
    
    if($solved_file_extension -eq "cpp"){
        $language_code = 5001  # 5001 (C++ 20 (gcc 12.2))
    }elseif($solved_file_extension -eq "py"){
        $language_code = 5078  # 5078 (Python (PyPy 3.10-v7.3.12))
    }else{
        Write-Host "Unsupported file extension: $solved_file_extension"
        exit
    }

    oj s $atcoder_url $solved_file_path -y --open -l $language_code
}

#####################################################################

# Get the file path from the command line arguments
$solved_file_path = $Args[0]  # Example: .\158\a_re.py
Write-Host "slolved_file_path : $solved_file_path"
$is_submit = [System.Convert]::ToBoolean($Args[1])
Write-Host "is_submit : $is_submit"

# Check if no arguments were provided
if ($Args.Count -eq 0) {
    Write-Host "No arguments provided. Please specify a file path."
    exit
}

# 問題の番号, 難易度, テストの結果を入れるファイル名
$solved_file = split-path $args[0] -leaf
$solved_directory = split-path $args[0] -parent # example: workspace/atcoder/contest/abc001A
$solved_file_components = $solved_file -split "\."
$solved_folder = split-path $solved_directory -leaf # example: abc001A
# $contest_number = $solved_folder.substring(0, $solved_folder.length-1)  # example: 158
# $problem_alphabet = $solved_directory.substring($solved_directory.length-1, 1).tolower()  # example: a
$success = $solved_folder -cmatch "^[a-z]+[0-9]*"
$contest_number = $Matches[0]  # example: abc158, dp, typical90
$success = $solved_folder -cmatch "[A-Z]+$"
$problem_alphabet = $Matches[0].tolower()  # example: a, b
$solved_file_name = ($solved_file_components[0]) -join "."  # 拡張子を除いたもの
$solved_file_extension = $solved_file_components[-1]  # 拡張子

Write-Host "solved_folder : $solved_file"
Write-Host "solved_file : $solved_file"
Write-Host "contest_number : $contest_number"
Write-Host "solved_file_name : $solved_file_name"
Write-Host "solved_file_extension : $solved_file_extension"

Write-Host "problem_alphabet : $problem_alphabet"

$test_directory = Join-Path -Path $solved_directory -ChildPath "samples"
Write-Host "test_directory : $test_directory"

$atcoder_url = "https://atcoder.jp/contests/$contest_number/tasks/${contest_number}_$problem_alphabet"
# if ([int]$contest_number.Substring(0, $contest_number.Length3) -le 14) {
#     $problem_alphabet_num = [byte][char]::ToUpper($problem_alphabet) - [byte][char]'A' + 1
#     $atcoder_url = "https://atcoder.jp/contests/$contest_number/tasks/${contest_number}_$problem_alphabet_num"
# }
Write-Host "atcoder_url : $atcoder_url"

if ($is_submit) {
    Test $test_directory $atcoder_url $solved_file_extension
    Submmit $atcoder_url $solved_file_path $solved_file_extension
} else {
    Test $test_directory $atcoder_url $solved_file_extension
}

