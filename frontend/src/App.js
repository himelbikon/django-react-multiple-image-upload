import { useState } from "react"
import axios from "axios"
import { Form, Button, Row, Col, Container, Image } from "react-bootstrap"

function App() {
  const [name, setName] = useState()
  const [file] = useState([])
  const [test, setTest] = useState("")

  const send = (event) => {
    console.log("send", file)
    const data = new FormData()
    data.append("name", name)

    file.map((image, i) => {
      data.append(`poster${i}`, image)
      console.log(`poster${i}`, image)
      return NaN
    })

    axios
      .post("http://127.0.0.1:8000", data)
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
            value={name}
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
              const img = e.target.files[0]
              file.push(img)
              setTest(test + "s")
            }}
          />
        </Form.Group>

        <Button onClick={send} variant="primary" type="button">
          Submit {file.length}
        </Button>
      </Form>

      {file.map((image) => (
        <div>{image.name}</div>
      ))}
    </Container>
  )
}

export default App
