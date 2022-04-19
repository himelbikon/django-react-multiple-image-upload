import { useState } from "react"
import axios from "axios"
import { Form, Button, Row, Col, Container, Image } from "react-bootstrap"

function App() {
  const [name, setName] = useState()
  const [file, setFile] = useState()

  const send = (event) => {
    console.log("send")
    const data = new FormData()
    data.append("name", name)
    data.append("poster", file)

    axios
      .post("http://127.0.0.1:8000/movies", data)
      .then((res) => console.log(res))
      .catch((err) => console.log(err))
  }

  return (
    <Container className="App">
      <Form>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Name"
            onChange={(e) => {
              const { value } = e.target
              setName(value)
            }}
          />
        </Form.Group>

        <Form.Group controlId="formFile" className="mb-3">
          <Form.Label>Default file input example</Form.Label>
          <Form.Control
            type="file"
            onChange={(e) => {
              const file = e.target.files[0]
              setFile(file)
            }}
          />
        </Form.Group>

        <Button onClick={send} variant="primary" type="button">
          Submit
        </Button>
      </Form>
    </Container>
  )
}

export default App
