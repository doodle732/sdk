*** Keywords ***

Chapter follows board reference structure
	Chapter has an overview
	Chapter has a specification of supported hardware
	Chapter covers programming and debugging
	Chapter covers testing
	Chapter lists hardware references

Chapter has an overview
	File Should Exist  ${CHAPTER_FILES}/overview.rst

Chapter has a specification of supported hardware
	File Should Exist  ${CHAPTER_FILES}/hardware.rst

Chapter covers programming and debugging
	File Should Exist  ${CHAPTER_FILES}/programming.rst

Chapter covers testing
	File Should Exist  ${CHAPTER_FILES}/testing.rst

Chapter lists hardware references
	File Should Exist  ${CHAPTER_FILES}/references.rst
