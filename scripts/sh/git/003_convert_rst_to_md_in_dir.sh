# v1
#FILES=*.rst
#for f in $FILES
#do
#  filename="${f%.*}"
#  echo "Converting $f to $filename.md"
#  `pandoc $f -f rst -t markdown -o $filename.md`
#done




# v2
# find . -name '*.rst' -exec pandoc {} -f rst -t markdown -o {}.md \;



# v3
# Non-recursively
#for rst in *.rst; do pandoc "$rst" -f rst -t markdown -o "${rst%.*}.md"; done

# Recursively (if your shell supports double-star globs)
for rst in **/*.rst; do pandoc "$rst" -f rst -t markdown -o "${rst%.*}.md"; done


# Recursively with delete rst
for rst in **/*.rst; do pandoc "$rst" -f rst -t markdown -o "${rst%.*}.md" && rm "$rst"; done