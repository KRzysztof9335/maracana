if [ -n "${SOURCED}" ]; then
  echo "Do not source twice ... Open new terminal"
  exit 1
fi

export SOURCED=1

echo "Setting up python environment ..."
make venv

echo "Setting up mongodb server ..."
mongod --port 27017 --dbpath ~/Desktop/db & &>/dev/null
