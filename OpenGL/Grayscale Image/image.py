import png

reader = png.Reader(filename='image1.png')
w, h, pixels, metadata = reader.read_flat()

if(metadata['alpha']):
	bytesPerPixel = 4
else:
	bytesPerPixel = 3

for linha in range(0,h):
	for coluna in range(0,w):
		posicao = bytesPerPixel*(w*linha+coluna)
		r = pixels[posicao]
		g = pixels[posicao+1]
		b = pixels[posicao+2]
		a = pixels[posicao+3]
		pixels[posicao] = int((r+g+b)/3)
		pixels[posicao+1] =  int((r+g+b)/3)
		pixels[posicao+2] = int((r+g+b)/3)

output = open('image2.png', 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, pixels)
output.close()
