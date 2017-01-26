package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
)

// git diff --word-diff=porcelain outs1 outs3 | sed -e 's/([^()]*)//g' | sed -e 's/([^()]*)//g' | grep -e '^+\|^-' | awk -F' ' 'NF>=6 {print}' | sed 's/^.//'

func main() {
	compareFiles("out", "out3")
}

func compareFiles(file1 string, file2 string) {
	changedLines := runCommand("./fix.sh " + file1 + " " + file2)
	fmt.Println(changedLines)

}

func runCommand(command string) string {
	var (
		cmdOut []byte
		err    error
	)
	commands := strings.Split(command, " ")
	cmdName := commands[0]
	cmdArgs := commands[1:len(commands)]
	if cmdOut, err = exec.Command(cmdName, cmdArgs...).CombinedOutput(); err != nil {
		fmt.Fprintln(os.Stderr, "Error running", cmdName, strings.Join(cmdArgs, " "), err)
		os.Exit(1)
	}
	return string(cmdOut)
}
